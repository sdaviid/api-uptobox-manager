from datetime import date
from pydantic import Field
from datetime import datetime
from app.models.schemas.base import baseSchema


class FileAddUpload(baseSchema):
    origin: str


class FileAdd(baseSchema):
    origin: str
    url: str



class FileDetail(baseSchema):
    id: int
    origin: str
    url: str
    md5_key: str
    date_created: datetime
