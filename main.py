from fastapi import FastAPI
from app import create_user_router
# from fastapi.responses import PlainTextResponse, JSONResponse
# from typing import Optional


def create_application() -> FastAPI :
    user_router = create_user_router()
    app = FastAPI()

    # add user_router to our app
    app.include_router(user_router)

    return app


app = create_application()