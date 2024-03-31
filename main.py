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



def get_user_info() -> User:

    content = {
        "name" : "testuser",
        "description" : "My bio description",
        "liked_posts" : None
    }

    return User(**content)


@app.get("/user/me", response_model=User)
def test_endpoint():

    user = get_user_info()

    return user
    


@app.get("/")
def home():
    return "Hello World"