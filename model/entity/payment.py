from sqlalchemy import Column, Integer, String, Boolean
from model.entity.base import Base
class Payment:

    def __init__(self, amount, payment_type, payment_date_time):
        self.id = None
        self.amount = amount
        self.payment_type = payment_type
        self.payment_date_time = payment_date_time

        class User(Base):
            __tablename__ = "user_tbl"
            id = Column(Integer, primary_key=True)
            amount = Column(String(30))
            payment_type = Column(String(30))
            payment_date_time = Column(String(30))

    def __repr__(self):
        return  str(self.__dict__)

