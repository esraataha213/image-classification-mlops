from image_classification.utils.common import read_yaml
from image_classification.entity.config_entity import DataIngestionConfig


class ConfigurationManager:

    def __init__(self, config_filepath="configs/config.yaml"):
        self.config = read_yaml(config_filepath)

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config["data"]

        data_ingestion_config = DataIngestionConfig(
            raw_data_path=config["raw_data_path"],
            train_data_path=config["train_data_path"],
            test_data_path=config["test_data_path"],
            prediction_data_path=config["prediction_data_path"],
        )

        return data_ingestion_config