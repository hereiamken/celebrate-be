from dotenv import load_dotenv
from supabase import Client
import schemas

import os


load_dotenv()

USER_NAME = os.getenv("USER_NAME")
PASS_WORD = os.getenv("PASS_WORD")

def create_user(supabase: Client, user: schemas.UserReq):
    # Insert user into the 'users' table, excluding the 'id' field (auto-incremented by the DB)
    try:
        response = supabase.table('users').insert({
            "name": user.name,
            "phoneNumber": user.phoneNumber,
            "wish": user.wish,
            "attend": user.attend,
            "cdcr": user.cdcr
        }).execute()

        # Check if user was added
        if response:
            # After insertion, the response will have the new user's 'id'
            new_user_id = response.data[0]['id']

            return {
                "data": {
                    "id": new_user_id,
                    "name": user.name,
                    "phoneNumber": user.phoneNumber,
                    "wish": user.wish,
                    "attend": user.attend,
                    "cdcr": user.cdcr
                }
            }
        else:
            return {"message": "User creation failed"}

    except Exception as e:
        print("Error: ", e)
        return {"message": "User creation failed"}


def get_users(supabase: Client):
    try:
        # Query the 'users' table from the Supabase database
        response = supabase.table('users').select("*").execute()
        if response:
            return {"data": response.data}
        else:
            return {"message": "Get users failed"}
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Users not found"}

# Delete a user


def delete_user(user_id: int, supabase: Client):
    user = supabase.from_("users").select("*").eq("id", user_id).execute()
    try:
        # Check if user exists
        if user:
            # Delete user
            supabase.from_("users")\
                .delete().eq("id", user_id)\
                .execute()
            return {"message": "User deleted successfully"}

        else:
            return {"message": "User deletion failed"}
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "User deletion failed"}


def update_user(user_id: int, user_req: schemas.UserReq, supabase: Client):
    try:
        user = supabase.from_("users").select("*").eq("id", user_id).execute()

        # Check if user exists
        if user:
            # Update user
            user = supabase.from_("users")\
                .update({"name": user_req.name,
                         "phoneNumber": user_req.phoneNumber,
                         "attend":  user_req.attend,
                         "cdcr": user_req.cdcr})\
                .eq("id", user_id).execute()
            if user:
                return {"message": "User updated successfully"}
        else:
            return {"message": "User update failed"}
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "User update failed"}

def verify_password(username, password):
    if username == USER_NAME and password == PASS_WORD:
        return True
    return False