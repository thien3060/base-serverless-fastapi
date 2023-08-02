from typing import Optional

from pydantic import BaseModel


class Paging(BaseModel):
    page: Optional[int] = 1
    page_size: Optional[int] = 20
