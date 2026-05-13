from fastapi import APIRouter, HTTPException, Response

from schemas.schemas import UserLoginSchema
from services.auth_service import config, security

authApp = APIRouter(tags=["Login"])


@authApp.post("/login")
def login(creds: UserLoginSchema, response: Response):

    if creds.username == "test" and creds.password == "test":
        token = security.create_access_token(uid="12345")

        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)

        return {"access_token": token}

    raise HTTPException(status_code=401, detail="Incorrect username or password")
