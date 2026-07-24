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