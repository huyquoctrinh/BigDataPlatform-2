import pandas as pd 
import os
import json 

def check_file_extension(filename):
    return filename.split('.')[-1]

def read_csv(file_path):
    return pd.read_csv(file_path)

def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)

class BatchIngestor:
    def __init__(self, data_dir, db_client):
        self.data_dir = data_dir
        self.file_extension = check_file_extension(data_dir)
        self.db_client = db_client

    # def csv_batch_ingest(self):
    def csv_batch_ingest(self, data_frame):
        pass

    def json_batch_ingest(self, data):
        pass

    def ingest(self):
        for file in os.listdir(self.data_dir):
            if check_file_extension(file) == self.file_extension:
                file_path = os.path.join(self.data_dir, file)
                if self.file_extension == "csv":
                    data = read_csv(file_path)
                    self.csv_batch_ingest(data)
                elif self.file_extension == "json":
                    data = read_json(file_path)
                    self.csv_batch_ingest(data)
                else:
                    return {
                        "status": "0",
                        "message": "Invalid file format"
                    }
        return {
            "status": "1",
            "message": "Data ingested successfully"
        }