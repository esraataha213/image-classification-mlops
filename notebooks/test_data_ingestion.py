from image_classification.config.configuration import ConfigurationManager
from image_classification.components.data_ingestion import DataIngestion

config = ConfigurationManager()

data_ingestion_config = config.get_data_ingestion_config()

data_ingestion = DataIngestion(data_ingestion_config)

data_ingestion.check_dataset_exists()