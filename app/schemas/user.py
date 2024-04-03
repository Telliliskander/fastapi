from pydantic import BaseModel, Field
from typing import Optional


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
