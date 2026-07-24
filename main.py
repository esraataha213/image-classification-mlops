from image_classification.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)

from image_classification.logger import logger


if __name__ == "__main__":

    try:
        logger.info("Pipeline started")

        pipeline = DataIngestionTrainingPipeline()

        pipeline.main()

        logger.info("Pipeline finished successfully")

    except Exception as e:
        logger.exception(e)
        raise e