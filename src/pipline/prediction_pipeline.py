from src.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from src.entity.s3_estimator import Proj1Estimator
from src.constants import *
from src.utils.main_utils import *
from src.entity.config_entity import ModelEvaluationConfig
import pandas as pd
class Prediction:
    def __init__(self,s3_eval:ModelEvaluationConfig):
    
        self.s3_eval = s3_eval
       
    def dict_df(self,input:dict):
        df = pd.DataFrame([input])
        return df


    def prediction_data(self,df:pd.DataFrame):
        path = self.s3_eval.s3_model_key_path
        s3 = Proj1Estimator(MODEL_BUCKET_NAME,path)
        model = s3.load_model()
       
        result = s3.predict(df)
        print(result)
        return result

