import time
from collections.abc import Callable

import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from router.auth import authApp
from router.router import database
from router.router import router as people_router
from services.auth_service import config

app = FastAPI()

app.include_router(people_router)
app.include_router(database)
app.include_router(authApp)


@app.middleware("http")
async def my_middleware(req: Request, call_next: Callable):

    start = time.perf_counter()

    # исключаем login endpoint
    if req.url.path == "/login":
        return await call_next(req)

    # получаем token из cookies
    token = req.cookies.get(config.JWT_ACCESS_COOKIE_NAME)

    # если токена нет
    if not token:
        return JSONResponse(status_code=401, content={"detail": "Token not found"})

    response = await call_next(req)

    end = time.perf_counter() - start
    print(f"Время работы запроса: {end=}")
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
