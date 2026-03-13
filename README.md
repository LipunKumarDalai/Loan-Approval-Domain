
# Loan Domain MLOps Pipeline

### End-to-End Machine Learning Project with CI/CD, Docker, AWS & MongoDB

![Python](https://img.shields.io/badge/Python-3.10-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Pipeline-green)
![MLOps](https://img.shields.io/badge/MLOps-End--to--End-orange)
![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20EC2%20%7C%20ECR-yellow)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![CI/CD](https://img.shields.io/badge/GitHub-Actions-purple)

An **End-to-End MLOps project** that demonstrates how a real-world machine learning system is built, deployed, and automated using modern industry tools.

This project implements a **complete ML lifecycle pipeline**, including:

* Data ingestion from **MongoDB Atlas**
* Data validation and transformation
* Model training and evaluation
* Model versioning in **AWS S3**
* Containerization with **Docker**
* Automated **CI/CD using GitHub Actions**
* Deployment on **AWS EC2**

The project simulates a **production-grade ML system architecture**.

---

# 📌 Project Architecture

```
Data Source (MongoDB Atlas)
        │
        ▼
Data Ingestion
        │
        ▼
Data Validation
        │
        ▼
Data Transformation
        │
        ▼
Model Trainer
        │
        ▼
Model Evaluation
        │
        ▼
Model Pusher (AWS S3)
        │
        ▼
Prediction Pipeline
        │
        ▼
Web Application (Streamlit)
        │
        ▼
Docker Container
        │
        ▼
CI/CD (GitHub Actions)
        │
        ▼
Deployment (AWS EC2)
```

---

# ⚙️ Tech Stack

### Programming

* Python 3.10

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy

### MLOps

* Docker
* GitHub Actions
* CI/CD Automation

### Cloud

* AWS S3 (Model Registry)
* AWS EC2 (Deployment)
* AWS ECR (Docker Registry)

### Database

* MongoDB Atlas

### Backend

* Streamlit

---

# 📂 Project Structure

```
vehicle-data-mlops
│
├── notebook/
│   ├── mongoDB_demo.ipynb
│   ├── EDA.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│   │
│   ├── configuration/
│   │   ├── mongo_db_connection.py
│   │   └── aws_connection.py
│   │
│   ├── entity/
│   │   ├── config_entity.py
│   │   ├── artifact_entity.py
│   │   ├── estimator.py
│   │   └── s3_estimator.py
│   │
│   ├── utils/
│   │   └── main_utils.py
│
├── pipeline/
│   ├── training_pipeline.py
│   └── prediction_pipeline.py
│
├── app.py
├── requirements.txt
├── setup.py
├── pyproject.toml
├── Dockerfile
├── .dockerignore
└── README.md
```

---

# 🚀 Getting Started

# 📊 Data Ingestion Pipeline

The ingestion pipeline:

* Connects to **MongoDB Atlas**
* Fetches raw dataset
* Converts key-value records into **Pandas DataFrame**
* Stores dataset inside **artifact directory**

Main modules involved:

```
data_access/
configuration/
entity/
components/data_ingestion.py
```

---

# 🔍 Data Validation

Validation checks include:

* Schema validation
* Column type validation
* Missing values
* Data consistency

Configuration defined in:

```
config/schema.yaml
```

---

# 🔧 Data Transformation

Feature engineering and preprocessing steps:

* Handling missing values
* Feature scaling
* Encoding categorical variables
* Preparing training dataset

---

# 🤖 Model Training

The model trainer:

* Splits dataset
* Trains ML models
* Selects best performing model
* Saves trained model artifact

---

# 📈 Model Evaluation

Compares new model with previous production model.

Threshold defined in constants:

```
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
```

If performance improves → model is pushed to **S3 Model Registry**

---
# 🔄 CI/CD Pipeline (GitHub Actions)

CI/CD automatically performs:

1️⃣ Build Docker Image
2️⃣ Push image to **AWS ECR**
3️⃣ Deploy to **EC2 instance**

Secrets required in GitHub:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
```

---

# 🖥️ EC2 Deployment

Launch EC2 instance:

```
Ubuntu Server 24.04
Instance: t2.medium
Storage: 30GB
```

Install Docker:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

---

# 🔗 Self Hosted Runner (GitHub → EC2)

Steps:

```
GitHub → Settings
Actions → Runner
New Self Hosted Runner
```

Run commands on EC2:

```
./config.sh
./run.sh
```

---

# 🌐 Application Access

Allow port **5000** in EC2 security group.

Access application:

```
http://<EC2-PUBLIC-IP>:5000
```

Training endpoint:

```
/training
```

---

# 📸 Application Features

✔ Train ML model from UI
✔ Predict using trained model
✔ Fully automated CI/CD deployment
✔ Cloud model registry

---

# 🧠 Key Learning Outcomes

This project demonstrates real **production ML system design** including:

* End-to-End ML pipelines
* Cloud infrastructure
* Model versioning
* CI/CD automation
* Docker containerization
* Scalable deployment architecture

---

# 👨‍💻 Author

**Lipu Daman**

Machine Learning | MLOps | Data Scientist

---

⭐ If you like this project, please **star the repository**!
