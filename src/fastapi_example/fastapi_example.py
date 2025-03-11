import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_index():
    return {"message": "Hello World", "time": time.time()}


@app.get("/time")
async def get_time():
    return {"time": time.ctime()}


@app.get("/hello")
async def get_hello():
    return {"hello": "how are you?"}
