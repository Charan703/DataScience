import os
from src.Data_Science import logger
from src.Data_Science.entity.config_entity import (DataValidationConfig)
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_schema = self.config.all_schema.keys()
            all_schema_datatypes = self.config.all_schema.values()

            # loop that checks if all columns are present in the data and if all columns are of the correct datatype
            for col, datatype in zip(all_schema, all_schema_datatypes):
                if data[col].dtype != datatype:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e