from image_classification.config.configuration import ConfigurationManager
from image_classification.components.data_validation import DataValidation

config = ConfigurationManager()

validation_config = config.get_data_validation_config()

validator = DataValidation(validation_config)

validator.validate_dataset()