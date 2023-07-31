import logging
from typing import Any

from fastapi import APIRouter

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/user")


@router.get("/")
async def get_ncbi_dashboard() -> Any:
    return {"name": "Test user"}
