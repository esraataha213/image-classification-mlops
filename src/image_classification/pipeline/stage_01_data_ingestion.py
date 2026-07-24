from image_classification.components.data_ingestion import DataIngestion
from image_classification.config.configuration import ConfigurationManager
from image_classification.logger import logger


class DataIngestionTrainingPipeline:

    def main(self):

        logger.info("Stage 01: Data Ingestion started")

        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(data_ingestion_config)

        data_ingestion.check_dataset_exists()

        logger.info("Stage 01 completed successfully")