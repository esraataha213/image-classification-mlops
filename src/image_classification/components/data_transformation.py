import tensorflow as tf

from image_classification.entity.config_entity import DataTransformationConfig
from image_classification.logger import logger


class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def get_data_generators(self):

        logger.info("Starting data transformation")

        train_dataset = tf.keras.utils.image_dataset_from_directory(
            self.config.train_data_path,
            image_size=(
                self.config.image_size,
                self.config.image_size
            ),
            batch_size=self.config.batch_size,
            shuffle=True
        )


        test_dataset = tf.keras.utils.image_dataset_from_directory(
            self.config.test_data_path,
            image_size=(
                self.config.image_size,
                self.config.image_size
            ),
            batch_size=self.config.batch_size,
            shuffle=False
        )


        normalization_layer = tf.keras.layers.Rescaling(1./255)


        train_dataset = train_dataset.map(
            lambda x, y: (normalization_layer(x), y)
        )

        test_dataset = test_dataset.map(
            lambda x, y: (normalization_layer(x), y)
        )


        train_dataset = train_dataset.prefetch(
            buffer_size=tf.data.AUTOTUNE
        )

        test_dataset = test_dataset.prefetch(
            buffer_size=tf.data.AUTOTUNE
        )


        logger.info("Data transformation completed")

        return train_dataset, test_dataset