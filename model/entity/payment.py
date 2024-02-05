from sqlalchemy import Column, Integer, String, Boolean
from model.entity.base import Base

class Payment(Base):
    __tablename__ = "stuff_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    model = Column(String(30))
    buy_price = Column(Integer)
    description = Column(String(100))


    def __init__(self,name,model,buy_price,description):
        self.id = None
        self.name = name
        self.model = model
        self.buy_price = buy_price
        self.description = description

    def __repr__(self):
        return str(self.__dict__)
