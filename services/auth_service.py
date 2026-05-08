from authx import AuthX, AuthXConfig
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

config = AuthXConfig()

config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]
config.JWT_COOKIE_CSRF_PROTECT = False


security = AuthX(config=config)


class UserLoginSchema(BaseModel):
    username: str
    password: str
