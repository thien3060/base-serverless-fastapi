import json
import logging
import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from pynamodb.exceptions import DoesNotExist, DeleteError

from app.models.user import User

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/user")


@router.get("")
async def list_user() -> Any:
    results = User.scan()
    return [dict(result) for result in results]


@router.get("/get")
async def get_user(user_id) -> Any:
    try:
        user = User.get(hash_key=user_id)
    except DoesNotExist:
        raise HTTPException(status_code=400, detail="User not found")

    return dict(user)


@router.post("/create")
async def create_user(user_name: str) -> Any:
    user = User(user_id=str(uuid.uuid1()), user_name=user_name)
    user.save()

    return dict(user)


@router.put("/update")
async def update_user(user_id: str, user_name: str) -> Any:
    try:
        user = User.get(hash_key=user_id)
    except DoesNotExist:
        raise HTTPException(status_code=400, detail="User not found")

    user.user_name = user_name
    user.save()

    return dict(user)


@router.delete("/delete")
async def create_user(user_id: str) -> Any:
    try:
        user = User.get(hash_key=user_id)
    except DoesNotExist:
        raise HTTPException(status_code=400, detail="User not found")
    try:
        user.delete()
    except DeleteError:
        raise HTTPException(status_code=400, detail="Unable to delete user")

    return {'statusCode': 204}
