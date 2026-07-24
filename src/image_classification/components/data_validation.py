import os

from image_classification.entity.config_entity import DataValidationConfig
from image_classification.logger import logger


class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_dataset(self):

        logger.info("Starting data validation...")

        train_classes = sorted(os.listdir(self.config.train_data_path))
        test_classes = sorted(os.listdir(self.config.test_data_path))

        logger.info(f"Train Classes: {train_classes}")
        logger.info(f"Test Classes: {test_classes}")

        if train_classes != test_classes:
            raise Exception("Train and Test classes do not match.")

        if len(train_classes) != 6:
            raise Exception(f"Expected 6 classes, found {len(train_classes)}.")

        logger.info("Data validation completed successfully.")