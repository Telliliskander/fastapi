from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()

@app.get("/test", response_class=JSONResponse)
def test_endpoint():
    return {
        "test key": "some key", 
        "another key" : "another value", 
        "nested key" : 
               {
                "internal_nested_key":"internal_nested_value"
                }
            }


@app.get("/")
def home():
    return "Hello World"