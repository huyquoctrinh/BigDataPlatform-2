import time
import threading
import os 
from tqdm import tqdm
import requests
from concurrent.futures import ThreadPoolExecutor
import logging

logging.basicConfig(filename='concurrent_test_1_thread.log', level=logging.INFO)
logger = logging.getLogger(__name__)

LIST_RPT = []
def create_test_data(path):
    # list_payload = []
    # list_files = []
    list_data = []
    for device in os.listdir(path):
        device_path = os.path.join(path, device)
        # print(device_path)
        for idx in tqdm(os.listdir(device_path)):
            idx_path = os.path.join(device_path, idx)
            # print(idx_path)
            for status in os.listdir(idx_path):
                status_path = os.path.join(idx_path, status)
                # print(status_path)
                for file in os.listdir(status_path):
                    
                    file_path = os.path.join(status_path, file)
                    # print(file_path)
                    # list_files.append(('audio_file', (file, open(file_path, 'rb'), 'audio/wav')))
                    payload = {
                        'db': path.repalce("_", " ")[0] + " dB",
                        'id': idx,
                        'device': device,
                        'status': status,
                        'tag': 'mimic-data'
                    }
                    list_data.append((payload, ('audio_file', (file, open(file_path, 'rb'), 'audio/wav'))))
                    # list_payload.append(payload)
    return list_data

def upload_file(data):
    payload, file = data
    files = [file]
    url = "http://34.28.159.51:5000/upload"
    headers = {}
    start = time.time()
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)
    end = time.time()
    LIST_RPT.append(end - start)
    # print(end - start)
    logger.info(f"Response time for the request: {end - start}")
    # print(response.text)


data_path = "-6_dB_pump"
list_data = create_test_data(data_path)[:2000]

print(len(list_data))

with ThreadPoolExecutor(max_workers=25) as executor:
    executor.map(upload_file, list_data)

print("Average results:", sum(LIST_RPT)/len(LIST_RPT))
