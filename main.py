from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()


class User(BaseModel):

    username : str = Field( # the fiel puts add attributes and put constraints over username.
        alias = "name",
        title = "The username",
        description = "this is the username of the user",
        min_length = 1,
        max_length = 20,
        default = None
    )
    description : str = "My bio description"
    liked_posts : Optional[list[int]]=None


class FullUserProfile(User):
    
    short_description : str
    long_bio : str



def get_user_info() -> FullUserProfile:

    profile_info = {
        "short_description": "My bio description",
        "long_bio" : "This is our longer bio",
    }
    

    user_content = {
        "liked_posts" : [1]*3,
        "profile_info" : profile_info
    }

    user = User(**user_content)

    fulluserprofile = {
        **profile_info,
        **user.dict()
    }

    return FullUserProfile(**fulluserprofile)


@app.get("/user/me", response_model=FullUserProfile)
def test_endpoint():

    user = get_user_info()

    return user
    


@app.get("/")
def home():
    return "Hello World"