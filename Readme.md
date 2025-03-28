# 🔍 Legal AI: Automated Legal Document Analysis Platform

## 🌟 Overview
The **Legal AI: Automated Legal Document Analysis Platform** simplifies the challenging process of analyzing legal documents using advanced technologies like **Next.js**, **NLP**, and **machine learning models**. This platform helps users extract key information, identify risks, and make informed decisions when handling contracts.

## ✨ Key Features
* **📃 Automated Document Analysis**: Automatically extracts and processes critical insights from legal documents, saving time and effort.
* **📖 Advanced Reading Comprehension**: Powered by the **SQuAD dataset**, allowing seamless information retrieval from contracts.
* **📑 CUAD Dataset Integration**: Incorporates 500 contracts to address frequently asked legal clauses.
* **✍️ Paraphrasing Model**: Built using the **T5-base model**, enabling intuitive clause interpretation through high-quality paraphrasing.
* **⭕ Sentiment Analysis**: Uses **TextBlob** for analyzing the sentiment and implications of contract clauses.
* **💻 User-Friendly Interface**: Built with **Next.js**, delivering an intuitive and responsive user experience.
* **🔗 Flask Server Integration**: Efficiently connects the frontend with machine learning models for robust backend processing.
* **📦 Docker Containerization**: Simplifies deployment through **Docker Compose** for quick setup and usage.

## 🚀 🖥️ Screenshots
### 💻 Frontend Interface
![Home Page](Screenshots/BrieflyLegalFrontentImg1.jpeg)

### 🔍 Analysis Results
![Process Image 1](Screenshots/BrieflyLegalImg1.jpeg)
![Process Image 2](Screenshots/BrieflyLegalImg2.jpeg)
![Process Image 3](Screenshots/BrieflyLegalImg3.jpeg)
![Process Image 4](Screenshots/BrieflyLegalImg4.jpeg)


## 🚀 Getting Started

### ⚙️ Manual Setup
1. **Clone the Repository**
```bash
git clone https://github.com/Zubair7102/Briefly-Legal.git
```

2. **Setup Frontend (Next.js)**
```bash
cd web
npm install
npm run dev
```

3. **Setup Backend (Flask)**
```bash
cd flask
pip install -r requirements.txt
flask run
```

4. **Access the Application**
Open your browser and navigate to `http://localhost:3000`

### 🐳 Docker Setup
1. **Install Docker** if not already installed.

2. **Run the Application**
```bash
docker-compose up
```

3. **Access the Application**
Open your browser and navigate to `http://localhost:3000`

## 🛠️ Technology Stack

| Technology | Description | 
|-----------|-------------|
| **Next.js** | React framework for building dynamic and responsive UIs |
| **Flask** | Lightweight Python web framework connecting the frontend with ML models |
| **PyTorch** | Powering the backend ML models for text processing |
| **TextBlob** | Sentiment analysis for contract clauses |
| **Docker** | Containerized deployment for seamless application setup |
| **SQuAD Dataset** | Dataset for building and validating the reading comprehension model |
| **CUAD Dataset** | Custom dataset featuring 500 legal contracts for clause extraction |
| **T5-base Model** | Pretrained model for paraphrasing and enhancing document understanding |

## ⚠️ Disclaimer
This platform assists users in understanding legal documents and identifying risks. **It is not a substitute for professional legal advice.** Consult a legal expert for critical decisions or contract signing.

## 🛡️ Technology Badges
[![Made with TypeScript](https://forthebadge.com/images/badges/made-with-typescript.svg)](https://forthebadge.com)
[![Made with Python](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Next.js](https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
