from enum import Enum
from typing import Optional, Any

from pydantic import BaseModel


class Paging(BaseModel):
    page: Optional[int] = 1
    page_size: Optional[int] = 20


class OperatorEnum(str, Enum):
    eq = "="
    gt = ">"
    lt = "<"
    neq = "!="


class BaseQuery(BaseModel):
    operator: OperatorEnum
    value: Any


OPERATOR_MAP = {
    OperatorEnum.eq: "==",
    OperatorEnum.gt: ">",
    OperatorEnum.lt: "<",
    OperatorEnum.neq: "!=",
}
