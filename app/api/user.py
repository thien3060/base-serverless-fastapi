import logging
import uuid

from fastapi import APIRouter, HTTPException, Depends
from pynamodb.exceptions import DoesNotExist, DeleteError

from app.models.user import User
from app.schemas.user import UserResponse, UserUpdateRequest, UserCreateRequest, UserGetRequest, UserDeleteRequest

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/user")


@router.get("")
async def list_user() -> list[UserResponse]:
    results = User.scan()
    return [dict(result) for result in results]


@router.get("/get")
async def get_user(request: UserGetRequest = Depends(UserGetRequest)) -> UserResponse:
    try:
        user = User.get(hash_key=request.user_id)
    except DoesNotExist:
        raise HTTPException(status_code=400, detail="User not found")

    return dict(user)


@router.post("/create")
async def create_user(request: UserCreateRequest) -> UserResponse:
    user = User(user_id=str(uuid.uuid1()), user_name=request.user_name)
    user.save()

    return dict(user)


@router.put("/update")
async def update_user(request: UserUpdateRequest) -> UserResponse:
    try:
        user = User.get(hash_key=request.user_id)
    except DoesNotExist:
        raise HTTPException(status_code=400, detail="User not found")

    user.user_name = request.user_name
    user.save()

    return dict(user)


@router.delete("/delete", status_code=204)
async def delete_user(request: UserDeleteRequest) -> None:
    try:
        user = User.get(hash_key=request.user_id)
    except DoesNotExist:
        raise HTTPException(status_code=400, detail="User not found")
    try:
        user.delete()
    except DeleteError:
        raise HTTPException(status_code=400, detail="Unable to delete user")

    return None
