import pytest
from app.services.user import UserService

@pytest.fixture
def _profile_infos():
    return  {
        0 : {
            "short_description": "My bio description",
            "long_bio" : "This is our longer bio",
        },
    }    
    
@pytest.fixture  
def _users_content():
    return {

        0 : {
            "liked_posts" : [1]*3,
        },
    }


@pytest.fixture
def user_service(_profile_infos, _users_content):
    user_service  = UserService(_profile_infos, _users_content)
    return user_service
