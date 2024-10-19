from sqlalchemy import TIMESTAMP, Table, Boolean, Column, Integer, String, text
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    phoneNumber = Column(String(15))
    wish = Column(String(500))
    attend = Column(Boolean, default=False)
    cdcr = Column(String(10))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
