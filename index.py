from fastapi import FastAPI
from supabase import Client, create_client
import admin
from database import SUPABASE_KEY, SUPABASE_URL

import response

app = FastAPI()
app.include_router(response.router)
app.include_router(admin.router)
# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
