from typing import Any, List

from fastapi import APIRouter

signup_router = APIRouter()

@signup_router.get("/signup",response_model=)
def signup_user() -> Any:
    return {'signup status':True}