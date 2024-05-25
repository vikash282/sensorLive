from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
#from sensor.entity.artifact_entity import ModelEvaluationArtifact,ModelPusherArtifact,ModelTrainerArtifact
#from sensor.entity.config_entity import ModelPusherConfig,ModelEvaluationConfig,ModelTrainerConfig


from sensor.exception import SensorException
import sys,os
from sensor.logger import logging
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
#from sensor.components.data_transformation import DataTransformation
#from sensor.components.model_trainer import ModelTrainer
#from sensor.components.model_evaluation import ModelEvaluation
#from sensor.components.model_pusher import ModelPusher

#from sensor.constant.training_pipeline import SAVED_MODEL_DIR


#from sensor.cloud_storage.s3_syncer import S3Sync
#from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME

class TrainPipeline:
   # is_pipeline_running = False
    #self.s3_sync = S3Sync()


    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()


    def start_data_ingestion(self)->DataIngestionArtifact:

        try:
            
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)

            logging.info("Starting data ingestion")

            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact
        
        except  Exception as e:
            raise  SensorException(e,sys)
        



    
    
    def start_data_validaton(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)

            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config = data_validation_config
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            return data_validation_artifact
        
        except  Exception as e:
            raise  SensorException(e,sys)







    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()




            data_validation_artifact=self.start_data_validaton(data_ingestion_artifact=data_ingestion_artifact)

            
        except Exception as e :    
            raise  SensorException(e,sys)