import os
from celery import Celery
import logging
from boto3 import client
import dotenv
import ast 
# from publisher.kafka_producer import Producer
import json

dotenv.load_dotenv()

logger = logging.getLogger(__name__)

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name='tasks.ingest_data')
def ingest_data_task(
    metadata_dict: dict
):
    logger.log(logging.INFO, f"Inserting new metadata for {metadata_dict['tenant_id']}")

    return metadata_dict

    # except Exception as e:
        # return False