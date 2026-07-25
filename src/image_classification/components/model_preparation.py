import tensorflow as tf
import os
from image_classification.entity.config_entity import ModelPreparationConfig
from image_classification.logger import logger


class ModelPreparation:

    def __init__(self, config: ModelPreparationConfig):
        self.config = config

    def build_model(self):

        logger.info("Building MobileNetV2 model...")

        base_model = tf.keras.applications.MobileNetV2(
            input_shape=(
                self.config.image_size,
                self.config.image_size,
                3,
            ),
            include_top=False,
            weights="imagenet",
        )

        base_model.trainable = False

        model = tf.keras.Sequential([
            base_model,
            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(
                self.config.num_classes,
                activation="softmax",
            ),
        ])

        model.compile(
            optimizer=tf.keras.optimizers.Adam(
                learning_rate=self.config.learning_rate
            ),
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )
        os.makedirs(self.config.model_dir, exist_ok=True)

        logger.info("Model created successfully.")

        return model