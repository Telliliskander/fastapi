from sample_requests.async_requests import sample_async_get_requests
from aioresponses import aioresponses
import pytest

async def test_sample_async_get_requests_works_properly():
    base_url = ''
    endpoint_prefix = ''
    user_id = 1

    with aioresponses() as m:
        m.get(
            f"{base_url}{endpoint_prefix}{user_id}",
            status = 200,
            headers = {"some-header" : "1"},
            payload = {"user": user_id}
        )

    satus_code, json_response = await sample_async_get_requests(base_url, endpoint_prefix, user_id)

    assert satus_code == 200
    assert json_response["user"] == user_id
    assert headers["some-header"] == "1"