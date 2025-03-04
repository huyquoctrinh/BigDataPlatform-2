from src.coredms.db_handler import AtlasClient
import pymongo

atlas_client = AtlasClient("mongodb://localhost:27017", "test")
atlas_client.ping()
collection = atlas_client.create_collection("amazon_collection")


