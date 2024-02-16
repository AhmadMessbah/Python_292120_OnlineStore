from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model.entity.base import Base



class Transaction(Base):
    __tablename__ = "transaction_tbl"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_tbl.id"))
    stuff_id = Column(Integer, ForeignKey("stuff_tbl.id"))
    quantity = Column(Integer)
    total_price = Column(Integer)
    date_time = Column(DateTime)

    user = relationship("User")
    stuff = relationship("Stuff")

    def __init__(self,user, stuff, quantity, total_price ,date_time):
        self.user = user
        self.stuff = stuff
        self.quantity = quantity
        self.date_time = datetime.now()
        self.total_price = total_price

    def __repr__(self):
        return str(self.__dict__)
