import uvicorn
from fastapi import FastAPI
from router.router import router as people_router

app = FastAPI()

app.include_router(people_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)