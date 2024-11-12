from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str = "mongodb+srv://patilharshal3558:yafPaa0Vz5UozzW2@cluster1.qtncqzd.mongodb.net/FastAPI"
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
