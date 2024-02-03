from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from model.entity.base import Base

class Storage(base):
    __tablename__ = "stuff_tbl"
    id = Column(Integer, primary_key=True)
    stuff_id = Column(Integer, ForeignKey("stuff_tbl.id"))
    stuff = Column(String(30))
    count = Column(Integer)

    stuff = relationship("Stuff")

    def __init__(self, stuff, count):
        self.id = None
        self.stuff = stuff
        self.count = count
    def __repr__(self):
        return str(self.__dict__)