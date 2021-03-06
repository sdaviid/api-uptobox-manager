from sqlalchemy import(
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.types import(
    Date,
    Boolean,
    Time,
    DateTime
)
from sqlalchemy.orm import(
    relationship,
    backref
)
from app.models.base import ModelBase
from app.core.database import Base
from datetime import datetime

from utils.utils import md5


class File(ModelBase, Base):
    __tablename__ = "file"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    origin = Column(String(255))
    url = Column(String(255))
    md5_key = Column(String(255))
    date_created = Column(DateTime, default=datetime.utcnow())


    @classmethod
    def add(cls, session, data):
        file = File()
        file.origin = data.origin
        file.url = data.url
        file.md5_key = md5(data.origin[data.origin.rindex('/')+1:])
        session.add(file)
        session.commit()
        session.refresh(file)
        return File.find_by_id(session=session, id=file.id)


    @classmethod
    def find_by_md5(cls, session, md5_key):
        return session.query(File).filter_by(md5_key=md5_key).first()

