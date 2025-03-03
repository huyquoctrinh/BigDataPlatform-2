from kafka import KafkaConsumer
import json
from db_handler import AtlasClient
import dotenv
import logging
import os 
from json import loads
from time import time
import multiprocessing
logging.basicConfig(
    filename = "./logs/data_updater.log",
    filemode = 'a',
    level = logging.INFO,
)

logger = logging.getLogger('data_updater')
dotenv.load_dotenv()

class DataUpdater:
    def __init__(self, 
        topic,
        kafka_broker = 'kafka:29092', 
    ):
        
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=kafka_broker,
            auto_offset_reset='earliest',
            value_deserializer=lambda m: loads(m.decode('utf-8'))
        )
        self.topic = topic
        self.atlas_client = AtlasClient(
            os.environ.get("ATLAS_URI"),
            os.environ.get("ATLAS_DB")
        )
    def consume(self):
        try:
            for message in self.consumer:
                metadata_dict = message.value
                start = time()
                self.atlas_client.insert(metadata_dict["device"], metadata_dict)
                end = time()
                logger.info(f"Time to insert data: {end - start}")
                logger.info(f"Inserted metadata for {metadata_dict}")
        except Exception as e:
            logger.error(f"Failed to insert metadata: {metadata_dict}")
            logger.error(e)
            pass

# if __name__ == "__main__":
logger.info('Data updater started')
data_updater = DataUpdater(topic='test')
num_processes = 4

for _ in range(num_processes):
    process = multiprocessing.Process(target=data_updater.consume)
    process.start()

    # data_updater.consume()