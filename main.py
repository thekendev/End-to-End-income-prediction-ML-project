from incomepredictor.src.logging import logger
from incomepredictor.src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from incomepredictor.src.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data ingestion stage"
try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
