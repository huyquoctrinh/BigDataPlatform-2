import json 
import pymongo
import os
import pandas as pd 

def check_file_extension(filename):
    return filename.split('.')[-1]

def read_csv(file_path):
    return pd.read_csv(file_path)

def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)
    