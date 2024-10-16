import pytest
from app import UserNotFound



@pytest.mark.asyncio 
async def test_delete_user_works_properly(user_service, valid_user_delete_id):

    await user_service.delete_user(valid_user_delete_id)
    assert valid_user_delete_id not in user_service.profile_infos
    assert valid_user_delete_id not in user_service.users_content

@pytest.mark.asyncio 
async def test_delete_invalid_user_raises_proper_exception(user_service, invalid_user_delete_id):
    with pytest.raises(Exception):

        await user_service.delete_user(invalid_user_delete_id)
        