import aiohttp 
import asyncio 


async def sample_async_get_requests(base_url : str, endpoint_prefix : str, user_id : int) -> (int, dict):
    async with aiohttp.ClientSession() as session:
        url = f"{base_url}{endpoint_prefix}{user_id}"
        async with session.get(url) as response:

            json_response = await response.json()
            status_code = response.status
            
            # some processing code

            return status_code, json_response

# asyncio.run(sample_async_get_requests())


async def sample_async_post_requests():

    sample_data_to_send = {
    "name" : "bob",
    "liked_posts" : [1,2,3,4],
    "short_description" : "some short description", 
    "long_bio" : "some long bio"
}

    async with aiohttp.ClientSession() as session:
        async with session.post("http://127.0.0.1:8000/user/0", json=sample_data_to_send) as response:
            print(response.status)
            print(response.headers)            
            print( await response.json())

asyncio.run(sample_async_post_requests())