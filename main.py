from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/test", response_class=PlainTextResponse)
def test_endpoint():
    return "hello this is a test"


@app.get("/")
def home():
    return "Hello World"