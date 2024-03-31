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



def get_user_info(user_id : str = "default") -> FullUserProfile:

    profile_infos = {
        "default" : {
            "short_description": "My bio description",
            "long_bio" : "This is our longer bio",
        },
        "user_1":{
            "short_description": "user 1's description",
            "long_bio" : "user 1's longer bio",

        }        
    }
    
    profile_info = profile_infos[user_id]

    users_content = {

        "default" : {
            "liked_posts" : [1]*3,
            "profile_info" : profile_infos["default"]
        },
        "user_1" : {
            "liked_posts" : [],
            "profile_info" : profile_info             
        }
    }
          
    user_content = users_content[user_id]
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



@app.get("/user/{user_id}", response_model=FullUserProfile)
def test_endpoint_by_id(user_id : str):

    user = get_user_info(user_id)

    return user


    


@app.get("/")
def home():
    return "Hello World"