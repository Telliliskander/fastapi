from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username : str
    description : str

def get_user_info() -> list[str, str]:

    username = "testuser"
    short_description = "my bio"

    return username, short_description


@app.get("/user/me", response_model=User)
def test_endpoint():

    username, short_description = get_user_info()

    user = User(username=username, description = short_description)

    return user
    



@app.get("/")
def home():
    return "Hello World"