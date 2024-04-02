from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional




app = FastAPI()

# ------------------- Variables ---------------------------------

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








#--------------------- Classes ----------------------------------

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


class CreateUserResponse(BaseModel):
    user_id : int


class MultipleUsersResponse(BaseModel):

    users : list[FullUserProfile]
    total : int

#--------------------- Functions ---------------------------------

def get_user_info(user_id : int = 0) -> FullUserProfile:

    profile_info = profile_infos[user_id]      
    user_content = users_content[user_id]
    
    user = User(**user_content)

    fulluserprofile = {
        **profile_info,
        **user.dict()
    }

    return FullUserProfile(**fulluserprofile)


def create_user(full_profile_info : FullUserProfile) -> int:

    global profile_infos
    global users_content

    new_user_id = len(profile_infos)
    liked_posts = full_profile_info.liked_posts
    short_description = full_profile_info.short_description
    long_bio = full_profile_info.long_bio 

    users_content[new_user_id] = {"liked_posts" : liked_posts}
    profile_infos[new_user_id] = {
        "short_description" : short_description,
        "long_bio" : long_bio
        }

    return new_user_id


def get_all_users_with_pagination(start : int, limit : int) -> tuple[list[FullUserProfile], int]:

    list_of_users = []
    keys = list(profile_infos.keys())  
    total = len(keys) 

    for index in range(0, len(keys), 1):

        if index < start :
            continue

        current_key = keys[index]
        user = get_user_info(current_key)
        list_of_users.append(user)

        if len(list_of_users) >= limit : 
            break

    return list_of_users, total






# --------------------- Endpoints ---------------------------------
@app.get("/user/me", response_model=FullUserProfile)
def test_endpoint():

    user = get_user_info()

    return user



@app.get("/user/{user_id}", response_model=FullUserProfile)
def test_endpoint_by_id(user_id : int):

    user = get_user_info(user_id)

    return user


@app.get("/users", response_model=MultipleUsersResponse)
def get_all_users_paginated(start : int = 0, limit : int = 2):
    users, total = get_all_users_with_pagination(start, limit)
    formatted_users = MultipleUsersResponse(users=users, total=total)
    return formatted_users


@app.post("/users", response_model=CreateUserResponse)
def add_user(full_profile_info : FullUserProfile):
    created_user_id = create_user(full_profile_info)
    return CreateUserResponse(user_id=created_user_id)


@app.get("/")
def home():
    return "Hello World"