from fastapi import FastAPI
from app.routes import auth, users

app = FastAPI(title="User Authentication API")

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the User Authentication API"}
