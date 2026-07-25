from image_classification.config.configuration import ConfigurationManager

config = ConfigurationManager()

model_config = config.get_model_preparation_config()

print(model_config)