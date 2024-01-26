from sqlalchemy import Column, Integer, String, Boolean
from model.entity.base import Base
class Stuff(Base):
    __tablename__ = "stuff_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    brand = Column(String(30))
    model = Column(String(30))
    buy_price = Column(Integer)
    description = Column(String(100))


    def __init__(self, name, brand, model, buy_price, description):
        self.name = name
        self.brand = brand
        self.model = model
        self.buy_price = buy_price
        self.description = description



