from fastapi import APIRouter, status
from crud import create_user
from database import get_supabase_client
import schemas


router = APIRouter(
    prefix='/wishs',
    tags=['Wishes']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_item(item: schemas.UserReq):
    supabase = get_supabase_client()
    res = create_user(supabase, item)
    return res
