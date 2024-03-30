from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()



def get_user_info()->(str,str) :
    username = "testuser"
    short_description = "my bio"
    return username, short_description


@app.get("/test", response_class=JSONResponse)
def test_endpoint():
    username, short_description = get_user_info()

    return {"username":"testuser", "short_description": "my bio"}
    



@app.get("/")
def home():
    return "Hello World"