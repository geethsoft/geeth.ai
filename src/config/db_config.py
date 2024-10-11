from pymongo import MongoClient


# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017"  # Update with your MongoDB URI
DB_NAME = "GEETHSOFT-HRMS"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
employees_collection = db["employees"]
