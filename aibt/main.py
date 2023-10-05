from fastapi import FastAPI,Depends
from typing import Annotated
from routes import api_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Test World"}


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/{commons}")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


app.include_router(api_router, prefix="/api/v1")