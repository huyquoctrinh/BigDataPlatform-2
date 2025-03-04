from pymongo import MongoClient

class AtlasClient ():
    def __init__ (
        self, 
        altas_uri, 
        dbname
    ):
        self.mongodb_client = MongoClient(altas_uri, w="majority")
        self.database = self.mongodb_client[dbname]

    def ping (self):
        self.mongodb_client.admin.command('ping')

    def get_collection (self, collection_name):
        collection = self.database[collection_name]
        return collection

    def check_exist_collection (self, collection_name):
        if collection_name in self.database.list_collection_names():
            return True
        return False

    def insert(self, collection_name, data):
        if not self.check_exist_collection(collection_name):
            self.database.create_collection(collection_name)

        collection = self.database[collection_name]
        collection.insert_one(data)
        return True

    def find (self, collection_name, filter = {}, limit=0):
        collection = self.database[collection_name]
        items = list(collection.find(filter=filter, limit=limit))
        return items