from datetime import datetime, timedelta
from typing import Any, Union
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import ValidationError
import jwt

SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '04102020'

reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)


def validate_token(http_authorization_credentials=Depends(reusable_oauth2)) -> str:
    """
    Decode JWT token to get username => return username
    """
    try:
        payload = jwt.decode(http_authorization_credentials.credentials,
                             SECRET_KEY, algorithms=[SECURITY_ALGORITHM])
        print(payload)
        if payload.get('exp') < datetime.now().timestamp():
            raise HTTPException(status_code=403, detail="Token expired")
        return payload.get('username')
    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=403,
            detail=f"Could not validate credentials",
        )


def generate_token(username: Union[str, Any]) -> str:
    expire = datetime.now() + timedelta(
        seconds=60 * 60 * 24 * 3  # Expired after 3 days
    )
    to_encode = {
        "exp": expire, "username": username
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,
                             algorithm=SECURITY_ALGORITHM)
    return encoded_jwt
