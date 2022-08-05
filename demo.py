from msilib import schema
from sklearn import pipeline
from housing.component import data_validation
from housing.config.configuration import Configuartion


from housing.pipeline.pipeline import Pipeline


from housing.exception import HousingException
from housing.logger import logging
from housing.component.data_transformation import DataTransformation
import os


def main():
    try:
        
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #data_validation_config = Configuartion().get_data_transformation_config()
        #print(data_validation_config) 
        #schema_file_path = r"C:\Users\karan\ML-Project\machine_learning_project\config\schema.yaml"
        #file_path = r"C:\Users\karan\ML-Project\machine_learning_project\housing\artifact\data_ingestion\2022-08-03-00-07-45\ingested_data\train\housing.csv"
        #df = DataTransformation.load_data(file_path=file_path, schema_file_path=schema_file_path)
        #print(df.columns)
        #print(df.dtypes)
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)
        
if __name__ == '__main__':
    main()
