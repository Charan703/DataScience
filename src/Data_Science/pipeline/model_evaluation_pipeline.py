from src.Data_Science.config.configuration import ConfigurationManager
from src.Data_Science.components.model_evaluation import ModelEvaluation
from src.Data_Science import logger

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        eval_config = config.get_model_evaluation_config()
        eval_config = ModelEvaluation(config=eval_config)
        eval_config.log_into_mlflow()