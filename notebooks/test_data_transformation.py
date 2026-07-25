from image_classification.config.configuration import ConfigurationManager
from image_classification.components.data_transformation import DataTransformation


config = ConfigurationManager()

transformation_config = config.get_data_transformation_config()


data_transformation = DataTransformation(
    transformation_config
)


train_dataset, test_dataset = data_transformation.get_data_generators()


for images, labels in train_dataset.take(1):
    print("Images shape:", images.shape)
    print("Labels shape:", labels.shape)