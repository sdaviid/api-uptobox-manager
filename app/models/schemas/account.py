from datetime import date
from pydantic import Field
from datetime import datetime
from app.models.schemas.base import baseSchema


class AccountAdd(baseSchema):
    api_key: str
    type_key: str



class AccountDetail(baseSchema):
    id: int
    api_key: str
    type_key: str
    date_created: datetime
