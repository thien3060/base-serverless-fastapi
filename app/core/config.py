from typing import List

from pydantic.networks import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Serverless FastAPI"
    API_PATH: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]
    AWS_DEFAULT_REGION: str = "ap-southeast-1"


settings = Settings()
