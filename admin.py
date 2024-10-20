from fastapi import APIRouter, Depends, HTTPException
from crud import delete_user, get_users, update_user, verify_password
from database import get_supabase_client
import schemas
from security import generate_token, validate_token

router = APIRouter(
    prefix='/admin',
    tags=['Admin side']
)

@router.get('/guests', dependencies=[Depends(validate_token)])
async def get_itemss():
    supabase = get_supabase_client()
    res = get_users(supabase)

    return res

@router.put("/guest", dependencies=[Depends(validate_token)])
def update_items(user_id: int, item: schemas.UserReq):
    supabase = get_supabase_client()
    res = update_user(user_id, item, supabase)

    return res

# Delete a user
@router.delete("/guest", dependencies=[Depends(validate_token)])
def delete_items(user_id: int):
    supabase = get_supabase_client()
    res = delete_user(user_id, supabase)

    return res

@router.post('/login')
def login(request_data: schemas.LoginRequest):
    print(f'[x] request_data: {request_data.__dict__}')
    if verify_password(username=request_data.username, password=request_data.password):
        token = generate_token(request_data.username)
        return {
            'token': token
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")