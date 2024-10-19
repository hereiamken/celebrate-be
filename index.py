from mangum import Mangum
from fastapi import FastAPI
from database import engine

import models
import response

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(response.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

handler = Mangum(app)
