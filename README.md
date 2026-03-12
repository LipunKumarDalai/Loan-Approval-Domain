.

🚗 Vehicle Data MLOps Project

A production-grade End-to-End MLOps pipeline for vehicle data processing, model training, and deployment using MongoDB, AWS, Docker, and CI/CD automation.

This project demonstrates how to build a complete machine learning lifecycle pipeline, starting from data ingestion to automated deployment on AWS EC2 using GitHub Actions.

📌 Project Architecture
Data Source
    │
    ▼
MongoDB Atlas
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
Model Registry (AWS S3)
    │
    ▼
Model Pusher
    │
    ▼
Prediction Pipeline
    │
    ▼
Flask Web App
    │
    ▼
Docker + CI/CD
    │
    ▼
AWS EC2 Deployment
🚀 Features

✔ Modular ML pipeline architecture
✔ MongoDB Atlas for dataset storage
✔ Automated data ingestion & validation
✔ Feature engineering pipeline
✔ Model training and evaluation
✔ Model registry using AWS S3
✔ Docker containerization
✔ CI/CD using GitHub Actions
✔ Self-hosted runner on AWS EC2
✔ End-to-end deployment automation

🧱 Project Setup
1️⃣ Create Project Template

Generate the project folder structure.

python template.py
📦 Package Configuration

Configure local packages using:

setup.py

pyproject.toml

For detailed explanation refer:

crashcourse.txt
🐍 Environment Setup

Create and activate a virtual environment.

conda create -n vehicle python=3.10 -y
conda activate vehicle

Install dependencies:

pip install -r requirements.txt

Verify installation:

pip list
🍃 MongoDB Atlas Setup
Step 1 — Create MongoDB Project

Sign up on MongoDB Atlas

Create a new project

Create a cluster

Choose:

Cluster Tier: M0 (Free)
Step 2 — Create Database User

Configure:

Username
Password
Step 3 — Network Access

Add IP:

0.0.0.0/0

This allows connection from anywhere.

Step 4 — Get Connection String

Navigate:

Cluster → Connect → Drivers

Select:

Driver : Python
Version: 3.6+

Example:

mongodb+srv://<username>:<password>@cluster.mongodb.net/
📊 Dataset Upload

Create a folder:

notebook/

Add dataset.

Create notebook:

mongoDB_demo.ipynb

Upload dataset to MongoDB using Python.

Verify data in:

MongoDB Atlas → Database → Browse Collections
🧾 Logging & Exception Handling

Custom modules implemented:

logger.py
exception.py

Test using:

demo.py
📊 Exploratory Data Analysis

Notebook added for:

Data exploration

Feature engineering

EDA_Feature_Engineering.ipynb
⚙ Data Ingestion Pipeline

Steps implemented:

MongoDB connection

Fetch data

Convert key-value records → Pandas DataFrame

Store artifacts

Main files involved:

configuration.mongo_db_connections.py
data_access.proj1_data.py
entity.config_entity.py
entity.artifact_entity.py
components.data_ingestion.py
🔑 MongoDB Environment Variable
Bash
export MONGODB_URL="mongodb+srv://<username>:<password>..."
echo $MONGODB_URL
PowerShell
$env:MONGODB_URL="mongodb+srv://<username>:<password>..."
echo $env:MONGODB_URL

Add artifacts folder to .gitignore.

🔍 Data Validation

Dataset validation using schema:

config/schema.yaml

Utility functions:

utils/main_utils.py
🔄 Data Transformation

Pipeline for:

Feature engineering

Data preprocessing

Feature scaling

Encoding

Includes:

entity/estimator.py
🤖 Model Training

Train ML models using transformed dataset.

Pipeline components:

components/model_trainer.py

Artifacts generated:

trained model

evaluation metrics

☁ AWS Setup

Login to AWS Console

Set region:

us-east-1
Create IAM User
IAM → Create User
Name: firstproj
Policy: AdministratorAccess

Create access key for CLI.

Set Environment Variables
Bash
export AWS_ACCESS_KEY_ID="AWS_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="AWS_SECRET_ACCESS_KEY"
PowerShell
$env:AWS_ACCESS_KEY_ID="AWS_ACCESS_KEY_ID"
$env:AWS_SECRET_ACCESS_KEY="AWS_SECRET_ACCESS_KEY"
🪣 AWS S3 Model Registry

Create bucket:

my-model-mlopsproj

Used for storing trained models.

Constants configuration:

MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
MODEL_BUCKET_NAME = "my-model-mlopsproj"
MODEL_PUSHER_S3_KEY = "model-registry"
📤 Model Evaluation & Model Pusher

Components:

Model Evaluation
Model Pusher

Purpose:

Compare new model with existing model

Push best model to S3 Model Registry

🔮 Prediction Pipeline

Prediction API implemented.

Main files:

app.py
prediction_pipeline.py

Routes:

/training
/predict
🌐 Web Application

Flask based application with:

templates/
static/

Used to perform real-time predictions.

🐳 Docker Setup

Create:

Dockerfile
.dockerignore

Build image:

docker build -t vehicleproj .

Run container:

docker run -p 5080:5080 vehicleproj
🔄 CI/CD Pipeline

GitHub Actions workflow added:

.github/workflows/aws.yaml

Pipeline includes:

Docker image build

Push image to AWS ECR

Deploy to EC2

📦 AWS ECR Setup

Create repository:

vehicleproj

Copy repository URI.

Used to store Docker images.

🖥 EC2 Server Setup

Launch instance:

Instance Name : vehicledata-machine
AMI           : Ubuntu Server 24.04
Instance Type : t2.medium
Storage       : 30GB
🐳 Install Docker on EC2
sudo apt-get update -y
sudo apt-get upgrade

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker ubuntu
newgrp docker
🔗 GitHub Self Hosted Runner

Setup runner:

GitHub → Settings → Actions → Runners

Run commands on EC2.

Start runner:

./run.sh

Runner status should appear:

idle
🔐 GitHub Secrets

Add secrets:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO

Location:

GitHub → Settings → Secrets → Actions
🚀 Deployment

CI/CD pipeline triggers automatically on:

git push
🌍 Application Access

Open browser:

http://<EC2_PUBLIC_IP>:5080
🎯 Training Endpoint

You can trigger model training using:

/training

Example:

http://<EC2_PUBLIC_IP>:5080/training
🛠 Tech Stack
Category	Tools
Language	Python
ML	Scikit-learn
Database	MongoDB Atlas
Cloud	AWS
Storage	AWS S3
Containerization	Docker
CI/CD	GitHub Actions
Deployment	AWS EC2
API	Flask
📂 Project Structure
src/
│
├── components
├── configuration
├── entity
├── data_access
├── pipeline
├── utils
│
notebook/
templates/
static/
artifacts/