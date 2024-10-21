from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import Client, create_client
import admin
from database import SUPABASE_KEY, SUPABASE_URL

import response

app = FastAPI()


# Add CORS middleware
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080",
    "https://celebrate-xi.vercel.app",
    "https://celebrate-trinhbh.vercel.app",
    "https://celebrate-kiendt.vercel.app",
    "https://celebrate-be.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
