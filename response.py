from fastapi import APIRouter, status, Depends
import models
from database import get_db
from sqlalchemy.orm import Session

import schemas

router = APIRouter(
    prefix='/wishs',
    tags=['Posts']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_item(item: schemas.UserCreate, db: Session = Depends(get_db)):
    post = models.User()
    post.name = item.name
    post.phoneNumber = item.phoneNumber
    post.wish = item.wish
    post.attend = item.attend
    post.cdcr = item.cdcr
    # db_post = models.User(**post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return [post]
