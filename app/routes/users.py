from fastapi import APIRouter, Depends, HTTPException, status, Body
from bson import ObjectId
from typing import List
from app.core.security import get_password_hash, oauth2_scheme
from app.core.database import users_collection
from app.models.user import UserCreate, User, UserUpdate
from app.utils.logger import logger

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
async def create_user(user: UserCreate): # Use the Pydantic model directly
    try:
        if users_collection.find_one({"email": user.email}):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        user_dict = user.model_dump() # or user.dict() if using Pydantic v1
        user_dict["password"] = get_password_hash(user_dict["password"])
        result = users_collection.insert_one(user_dict)
        user_dict["id"] = str(result.inserted_id)
        logger.info(f"Created new user: {user.email}")
        return user_dict
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/", response_model=List[User])
async def get_users(token: str = Depends(oauth2_scheme)):
    users = []
    for user in users_collection.find():
        user["id"] = str(user["_id"])
        del user["_id"]
        del user["password"]
        users.append(user)
    return users

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str, token: str = Depends(oauth2_scheme)):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    user["id"] = str(user["_id"])
    del user["_id"]
    del user["password"]
    return user
