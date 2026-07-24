from image_classification.components.data_ingestion import DataIngestion
from image_classification.components.data_validation import DataValidation

from image_classification.config.configuration import ConfigurationManager
from image_classification.logger import logger


class DataIngestionTrainingPipeline:

    def main(self):

        logger.info("Stage 01: Data Ingestion started")

        config = ConfigurationManager()


        # Data Ingestion
        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(data_ingestion_config)

        data_ingestion.check_dataset_exists()


        logger.info("Data Ingestion completed")


        # Data Validation
        logger.info("Stage 02: Data Validation started")

        validation_config = config.get_data_validation_config()

        validator = DataValidation(validation_config)

        validator.validate_dataset()


        logger.info("Data Validation completed")

        logger.info("Pipeline completed successfully")