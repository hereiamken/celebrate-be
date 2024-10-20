from dotenv import load_dotenv
from supabase import create_client, Client
import os


load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY")

# Initialize Supabase client
def get_supabase_client() -> Client:
    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    print(client)
    return client
