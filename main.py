from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def test_endpoint():
    return "hello this is a test"


@app.get("/")
def home():
    return "Hello World"