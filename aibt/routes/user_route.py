from typing import Any, List

from fastapi import APIRouter
# from fastapi.encoders import jsonable_encoder
# from pydantic.networks import EmailStr
# from sqlalchemy.orm import Session

# from app import crud, models, schemas
# from app.api import deps
# from app.core.config import settings
# from app.utils import send_new_account_email

user_router = APIRouter()


@user_router.get("/")
def read_users() -> Any:
    return {'users':"users_data"}

# user_router.include_router(user_router,prefix="/users")

