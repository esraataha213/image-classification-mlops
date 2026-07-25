from image_classification.config.configuration import ConfigurationManager
from image_classification.components.model_preparation import ModelPreparation


config = ConfigurationManager()

model_config = config.get_model_preparation_config()

builder = ModelPreparation(model_config)

model = builder.build_model()

model.summary()