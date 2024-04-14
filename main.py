from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app import create_user_router
# from fastapi.responses import PlainTextResponse, JSONResponse
# from typing import Optional
from app.services.exceptions import UserNotFound
from app.services.exception_handlers import add_exception_handlers

def create_application() -> FastAPI :

    
    user_router = create_user_router()
    app = FastAPI()

    # add user_router to our app
    app.include_router(user_router)
    
    add_exception_handlers(app)

    return app


app = create_application()