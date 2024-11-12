from pymongo import MongoClient
from app.core.security import get_password_hash
from app.config import settings

def create_admin_user():
    client = MongoClient(settings.MONGODB_URL)
    db = client.auth_db
    users_collection = db.users

    admin_user = {
        "email": "admin@example.com",
        "full_name": "Admin User",
        "password": get_password_hash("admin123"),
        "role": "admin"
    }

    if not users_collection.find_one({"email": admin_user["email"]}):
        users_collection.insert_one(admin_user)
        print("Admin user created successfully")
    else:
        print("Admin user already exists")

if __name__ == "__main__":
    create_admin_user()
