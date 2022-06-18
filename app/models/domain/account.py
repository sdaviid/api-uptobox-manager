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


class Account(ModelBase, Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    api_key = Column(String(255))
    type_key = Column(String(255))
    date_created = Column(DateTime, default=datetime.utcnow())


    @classmethod
    def add(cls, session, data):
        account = Account()
        account.api_key = data.api_key
        account.type_key = data.type_key
        session.add(account)
        session.commit()
        session.refresh(account)
        return Account.find_by_id(session=session, id=account.id)


    @classmethod
    def find_upload_api(cls, session):
        return session.query(cls).filter_by(type_key='U').first()


    @classmethod
    def find_premium_api(cls, session):
        return session.query(cls).filter_by(type_key='D').first()
