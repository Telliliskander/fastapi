from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app import create_user_router, UserNotFound, add_exception_handlers
# from fastapi.responses import PlainTextResponse, JSONResponse
# from typing import Optional




def create_profile_infos_and_users_content():

    profile_infos = {
        0 : {
            "short_description": "My bio description",
            "long_bio" : "This is our longer bio",
        },
    }        


    users_content = {

        0 : {
            "liked_posts" : [1]*3,
        },
    }
    return profile_infos, users_content 


def create_application() -> FastAPI :

    profile_infos, users_content = create_profile_infos_and_users_content()
    user_router = create_user_router(profile_infos, users_content)
    app = FastAPI()

    # add user_router to our app
    app.include_router(user_router)
    
    add_exception_handlers(app)

    return app


app = create_application()