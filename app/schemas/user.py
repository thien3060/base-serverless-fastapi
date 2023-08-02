from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    user_name: str


class UserUpdateRequest(BaseModel):
    user_id: str
    user_name: str


class UserResponse(BaseModel):
    user_id: str
    user_name: str
    createdAt: str
    updatedAt: str


class UserGetRequest(BaseModel):
    user_id: str


class UserDeleteRequest(BaseModel):
    user_id: str
