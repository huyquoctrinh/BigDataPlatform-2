import csv
import pandas as pd 
from tqdm import tqdm
import requests
import json
import os

def upload_file(url, csv_file, tenant_id):
    payload = {
        'tenant_id': tenant_id
    }
    response = requests.post(url, data = payload, files={"data_file": open(csv_file, "rb")})
    return response

if __name__ == "__main__":
    url = "http://localhost:5000/upload"
    csv_file = "dataset/amazon_reviews_multilingual_US_v1_00.tsv/amazon_reviews_multilingual_US_v1_00.tsv"
    # df = pd.read_csv("dataset/amazon_reviews_multilingual_US_v1_00.tsv/amazon_reviews_multilingual_US_v1_00.tsv", sep="\t", on_bad_lines="skip")
    # print(df.columns)

    # batch_size = 100
    # df_update = df[:batch_size]
    # print(len(df_update), df.columns)
    response = upload_file(url, csv_file, "tenant1")
    print(response)