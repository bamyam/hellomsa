from datetime import datetime

from sqlalchemy import Integer, Column, String, Text, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    mno = Column(Integer, primary_key=True, autoincrement=True, index=True)
    userid = Column(String(18), nullable=False)
    passwd = Column(String(128), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    #regdate = Column(DateTime, default=datetime.now(), nullable=True)
    # 선언한 시간대로만 들어가기 때문에 이 코드는 좋지 않음
    #regdate = Column(String(20), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    regdate = Column(String(20))