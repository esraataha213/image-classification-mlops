import os

from image_classification.entity.config_entity import DataIngestionConfig
from image_classification.logger import logger


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def check_dataset_exists(self):

        logger.info("Checking dataset paths...")

        paths = [
            self.config.raw_data_path,
            self.config.train_data_path,
            self.config.test_data_path,
            self.config.prediction_data_path,
        ]

        for path in paths:

            if os.path.exists(path):
                logger.info(f"Found: {path}")
            else:
                raise FileNotFoundError(f"Dataset path not found: {path}")

        logger.info("Dataset validation completed successfully.")