import aiohttp 
import asyncio 


async def sample_async_get_requests():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8000/user/0") as response:
            print(response.status)
            print(response.headers)            
            print( await response.json())

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