from pymongo import MongoClient
from app.config import settings

client = MongoClient(settings.MONGODB_URL)
db = client.auth_db
users_collection = db.users
