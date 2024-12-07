from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
from paraphrase import paraphrase
from predict import run_prediction
from io import StringIO
import json
from flask_cors import CORS
import chardet

app = Flask(__name__)
CORS(app)
answers = []

def load_questions_short():
    questions_short = []
    try:
        with open('data/questions_short.txt', encoding="utf8") as f:
            questions_short = f.readlines()
    except Exception as e:
        print(f"Error loading questions_short.txt: {e}")
    return questions_short

def getContractAnalysis(selected_response):
    print(f"Analyzing response: {selected_response}")
    if selected_response == "":
        return "No answer found in document"
    
    try:
        blob = TextBlob(selected_response)
        polarity = blob.sentiment.polarity
        print(f"Sentiment polarity: {polarity}")

        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        print(f"Error analyzing text: {e}")
        return "Analysis error"

questions_short = load_questions_short()

@app.route('/questionsshort')
def getQuestionsShort():
    return jsonify(questions_short)

@app.route('/contracts/', methods=["POST"])
def getContractResponse():
    try:
        file = request.files["file"]
        question = request.form['question']

        if not file or not question:
            return jsonify({"message": "File or question missing"}), 400

        # Detect file encoding
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding'] or 'utf-8'  # Fallback to 'utf-8' if None

        print(f"Detected encoding: {encoding}")

        try:
            # Read the file with the detected encoding
            stringio = StringIO(raw_data.decode(encoding, errors="ignore"))
            response = []
            answer = ""

            # Read file as string:
            paragraph = stringio.read()

            if paragraph and question:
                print('Getting predictions...')
                predictions = run_prediction([question], paragraph, 'marshmellow77/roberta-base-cuad', n_best_size=5)
                answer = []
                if predictions['0'] == "":
                    answer.append({
                        "answer": 'No answer found in document',
                        "probability": ""
                    })
                else:
                    # If predictions are available, process them
                    with open("nbest.json", encoding="utf8") as jf:
                        data = json.load(jf)
                        for i in range(5):
                            answer.append({
                                "answer": data['0'][i]['text'],
                                "probability": f"{round(data['0'][i]['probability']*100, 1)}%",
                                "analyse": getContractAnalysis(data['0'][i]['text'])
                            })
                return jsonify(answer)
            else:
                return jsonify({"message": "Unable to call model, please select question and contract"}), 400

        except Exception as e:
            print(f"Error processing file content: {e}")
            return jsonify({"message": "Error processing file content"}), 500

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"message": "File processing error"}), 500

@app.route('/contracts/paraphrase/<path:selected_response>', methods=['GET'])
def getContractParaphrase(selected_response):
    print(f"Selected response for paraphrase: {selected_response}")
    if not selected_response:
        return jsonify({"message": "No answer found in document"})
    
    try:
        print('Getting paraphrases...')
        paraphrases = paraphrase(selected_response)
        print(f"Paraphrases: {paraphrases}")
        return jsonify(paraphrases)
    except Exception as e:
        print(f"Error in paraphrase processing: {e}")
        return jsonify({"message": "Error processing paraphrase request"}), 500

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        question = request.form['selected_response']
        if not question:
            return jsonify({"message": "Question is missing"}), 400

        with open('responses.json', 'r') as file:
            responses = json.load(file)
            for response in responses:
                if response['question'] == question:
                    return jsonify({"answer": response['answer']})

        return jsonify({"message": "Response not found"}), 404

    except Exception as e:
        print(f"Error reading responses: {e}")
        return jsonify({"message": "Error processing request"}), 500

if __name__ == '__main__':
    app.run(debug=True)
