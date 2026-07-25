from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    raw_data_path: str
    train_data_path: str
    test_data_path: str
    prediction_data_path: str


@dataclass(frozen=True)
class DataValidationConfig:
    train_data_path: str
    test_data_path: str


@dataclass(frozen=True)
class TrainingConfig:
    image_size: int
    batch_size: int
    epochs: int
    learning_rate: float
    num_classes: int
    
@dataclass(frozen=True)
class ModelPreparationConfig:
    image_size: int
    num_classes: int
    learning_rate: float
    model_dir: str
    model_name: str