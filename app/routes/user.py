from fastapi import APIRouter, HTTPException
from app.schemas.user import (FullUserProfile, 
                             MultipleUsersResponse, 
                             CreateUserResponse)
from app.services.user import UserService
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(filename="log.txt")
logger.setLevel(logging.INFO) # levels debug -> info -> warning -> error -> critical




def create_user_router() -> APIRouter:
    user_router = APIRouter(prefix="/user",
                            tags=["user"])

    user_service = UserService()


    @user_router.get("/{user_id}", response_model=FullUserProfile)
    async def get_user_by_id(user_id : int):

        try :
            fulluserprofile = await user_service.get_user_info(user_id)

        except KeyError:
            logger.error(f"Invalid user id {user_id} was requested")
            raise HTTPException(status_code = 404, detail = "User doesn't exist")

        return fulluserprofile


    @user_router.get("/all", response_model=MultipleUsersResponse)
    async def get_all_users_paginated(start : int = 0, limit : int = 2):
        users, total = await user_service.get_all_users_with_pagination(start, limit)
        formatted_users = MultipleUsersResponse(users=users, total=total)
        return formatted_users


    @user_router.post("/", response_model=CreateUserResponse, status_code = 201)
    async def add_user(full_profile_info : FullUserProfile):
        created_user_id = await user_service.create_update_user(full_profile_info)
        print(user_service.create_update_user.__doc__)
        return CreateUserResponse(user_id=created_user_id)


    @user_router.put("/{user_id}")
    async def update_user(user_id : int, full_profile_info : FullUserProfile):

        await user_service.create_update_user(full_profile_info, user_id)


    @user_router.delete("/{user_id}")
    async def remove_user(user_id : int) -> None:
        logger.info(f"About to delete user id {user_id}")
        logger.debug(f"this is a debug log")
        try :
            await user_service.delete_user(user_id)
        except KeyError:
            raise HTTPException(status_code=404, detail=f"User with id {user_id} doesn't exist")
#            raise HTTPException(status_code=404, detail={"msg" : "User doesn't exist", "id" : {user_id}})
    return user_router