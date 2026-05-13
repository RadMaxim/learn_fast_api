import asyncio
import time
from collections.abc import Callable

import cv2
import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse, StreamingResponse

from router.auth import authApp
from router.router import database
from router.router import router as people_router
from services.auth_service import config

app = FastAPI()

app.include_router(people_router)
app.include_router(database)
app.include_router(authApp)


@app.get("/video")
def video():

    def generate_frames():
        cap = cv2.VideoCapture(0)

        try:
            while True:
                success, frame = cap.read()

                if not success:
                    break

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                success, buffer = cv2.imencode(".jpg", gray)

                if not success:
                    continue

                frame_bytes = buffer.tobytes()

                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
                )

        finally:
            cap.release()

    return StreamingResponse(
        generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame"
    )


async def generator():

    for i in range(10):
        yield f"Message {i}\n"

        await asyncio.sleep(1)


@app.get("/stream")
async def stream():

    return StreamingResponse(generator(), media_type="text/plain")


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
