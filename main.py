import uvicorn
from fastapi import FastAPI

from router.auth import authApp
from router.router import database
from router.router import router as people_router

app = FastAPI()

app.include_router(people_router)
app.include_router(database)
app.include_router(authApp)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
