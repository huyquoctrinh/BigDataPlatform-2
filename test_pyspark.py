from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("MongoDBIntegration") \
    .config("spark.mongodb.write.connection.uri", "mongodb://localhost:27017") \
    .config("spark.mongodb.write.database", "amazon_review") \
    .config("spark.mongodb.write.collection", "amazon_tenant") \
    .getOrCreate()

# Sample DataFrame
data = [("Alice", 25), ("Bob", 30)]
df = spark.createDataFrame(data, ["name", "age"])

# Write to MongoDB
df.write \
    .format("mongodb") \
    .mode("append") \
    .option("database", "mydatabase") \
    .option("collection", "mycollection") \
    .save()

print("Data written to MongoDB successfully!")
