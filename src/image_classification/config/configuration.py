from image_classification.utils.common import read_yaml
from image_classification.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelPreparationConfig,
)


class ConfigurationManager:

    def __init__(self, config_filepath="configs/config.yaml"):
        self.config = read_yaml(config_filepath)


    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config["data"]

        return DataIngestionConfig(
            raw_data_path=config["raw_data_path"],
            train_data_path=config["train_data_path"],
            test_data_path=config["test_data_path"],
            prediction_data_path=config["prediction_data_path"],
        )
    
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:

        config = self.config["validation"]

        data_validation_config = DataValidationConfig(
            train_data_path=config["train_data_path"],
            test_data_path=config["test_data_path"],
        )

        return data_validation_config
    


    def get_data_validation_config(self) -> DataValidationConfig:

        config = self.config["validation"]

        return DataValidationConfig(
            train_data_path=config["train_data_path"],
            test_data_path=config["test_data_path"],
        )


    def get_data_transformation_config(self) -> DataTransformationConfig:

        data = self.config["data"]
        training = self.config["training"]

        return DataTransformationConfig(
            train_data_path=data["train_data_path"],
            test_data_path=data["test_data_path"],
            image_size=training["image_size"],
            batch_size=training["batch_size"],
        )


    def get_model_preparation_config(self) -> ModelPreparationConfig:

        training = self.config["training"]

        return ModelPreparationConfig(
            image_size=training["image_size"],
            num_classes=training["num_classes"],
            learning_rate=training["learning_rate"],
            model_dir=training["model_dir"],
            model_name=training["model_name"],
        )