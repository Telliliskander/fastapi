from fastapi import APIRouter
from app.schemas.user import (FullUserProfile, 
                             MultipleUsersResponse, 
                             CreateUserResponse)
from app.services.user import UserService



def create_user_router() -> APIRouter:
    user_router = APIRouter()

    user_service = UserService()



    @user_router.get("/user/me", response_model=FullUserProfile)
    async def test_endpoint():

        user = await user_service.get_user_info()

        return user


    @user_router.get("/user/{user_id}", response_model=FullUserProfile)
    async def test_endpoint_by_id(user_id : int):

        user = await user_service.get_user_info(user_id)

        return user


    @user_router.get("/users", response_model=MultipleUsersResponse)
    async def get_all_users_paginated(start : int = 0, limit : int = 2):
        users, total = await user_service.get_all_users_with_pagination(start, limit)
        formatted_users = MultipleUsersResponse(users=users, total=total)
        return formatted_users


    @user_router.post("/users", response_model=CreateUserResponse)
    async def add_user(full_profile_info : FullUserProfile):
        created_user_id = await user_service.create_update_user(full_profile_info)
        print(user_service.create_update_user.__doc__)
        return CreateUserResponse(user_id=created_user_id)


    @user_router.put("/user/{user_id}")
    async def update_user(user_id : int, full_profile_info : FullUserProfile):

        await user_service.create_update_user(full_profile_info, user_id)


    @user_router.delete("/user/{user_id}")
    async def remove_user(user_id : int) -> None:

        await user_service.delete_user(user_id)


    @user_router.get("/")
    def home():
        return "Hello World"
    
    return user_router