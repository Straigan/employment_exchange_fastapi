from fastapi import FastAPI
import uvicorn

from endpoints import users, auth, jobs
from db.base import database

app = FastAPI(title="Employe exchange")
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(auth.router, prefix="/jobs", tags=["jobs"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.diconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)