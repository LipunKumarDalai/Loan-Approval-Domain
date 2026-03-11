import streamlit as st 
import pandas as pd
import numpy as np
import joblib
import boto3
import dill
from io import BytesIO
from datetime import datetime
from src.utils.main_utils import *
from src.components.model_evaluation import ModelEvaluation
from src.entity.artifact_entity import ModelTrainerArtifact,DataIngestionArtifact
from src.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from src.pipline import prediction_pipeline
from src.entity.config_entity import ModelEvaluationConfig

class App:
    def __init__(self,pipeline:prediction_pipeline):
      
        self.pipeline = pipeline
    def header_icons_inputs(self):
        st.header("Loan Approval App")
        
        df = pd.read_csv("notebook/loan_data.csv")

        gender = df.groupby(["person_gender"]).size().to_dict().keys()
        edu_dict = df.groupby(["person_education"]).size().to_dict().keys()
        own_dict = df.groupby(["person_home_ownership"]).size().to_dict().keys()
        intent_dict = df.groupby(["loan_intent"]).size().to_dict().keys()

        gend = st.selectbox("Applicant's Gender",gender)
        education = st.selectbox("Applicant's Education",edu_dict)
        ownership = st.selectbox("Applicant's Ownership",own_dict)
        intent = st.selectbox("Loan Intent",intent_dict)
        previous_loan = st.radio("Previous Loan Default in file",["Yes","No"])

        exp = st.slider("Applicants Experience",min_value=0,max_value=76)
        age = st.number_input("Applicants Age",min_value=20,max_value=94)
        loan_int = st.slider("Interest Rate",min_value=4.0,max_value=20.0)
        loan_amt = st.number_input("Loan Amount (USD)",min_value=5000,max_value=35000)
        cred_hist = st.slider("Credit history length",min_value=2.0,max_value=30.0,step=1.0)
        persons_inc =st.number_input("Applicant's Income (USD per Annum)",min_value=8000,max_value=8000766)
        credits = st.number_input("Credit Score",min_value=300,max_value=850)
        loan_per_inc = round(loan_amt/persons_inc,2)
   
        dictt = {
            
    "person_age": age,
    "person_gender": gend,
    "person_education": education,
    "person_income": persons_inc,
    "person_emp_exp": exp,
    "person_home_ownership": ownership,
    "loan_amnt": loan_amt,
    "loan_intent": intent,
    "loan_int_rate": loan_int,
    "loan_percent_income": loan_per_inc,
    "cb_person_cred_hist_length": cred_hist,
    "credit_score": credits,
    "previous_loan_defaults_on_file": previous_loan
}
             
        
        return dictt
    
    def prediction_pipe(self):

        icons = self.header_icons_inputs()

        if st.button("SUBMIT"):

            df = self.pipeline.dict_df(icons)

            result = self.pipeline.prediction_data(df)

            if result[0] == 1:
                st.success("Loan Approved")
            else:
                st.error("Applicant not eligible")

def main():

    pipeline = prediction_pipeline.Prediction(ModelEvaluationConfig)
    app = App(pipeline)

    app.prediction_pipe()


if __name__ == "__main__":
    main()


       
    




