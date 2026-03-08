# from src.logger import logging

# logging.debug("Yo")



from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()