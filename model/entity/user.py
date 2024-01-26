from sqlalchemy import Column, Integer, String, Boolean
from model.entity.base import Base


class User(Base):
    __tablename__ = "user_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    username = Column(String(30))
    password = Column(String(8))
    phone = Column(String(11))
    status = Column(Boolean)


    def __init__(self, name, family, username, password, phone, status=True):
        self.id = None
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.phone = phone
        self.status = status

    def __repr__(self):
        return str(self.__dict__)
