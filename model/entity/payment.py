from sqlalchemy import Column, Integer, String, Boolean
from model.entity.base import Base

class Payment(Base):
    __tablename__ = "payment_tbl"
    id = Column(Integer, primary_key=True)
    user_id = column(Integer,foreingKey("user.id")
    name = Column(String(30))
    model = Column(String(30))
    buy_price = Column(Integer)
    description = Column(String(100))


    def __init__(self,name,,user_id,model,buy_price,description):
        self.id = None
        self.user_id = user_id
        self.name = name
        self.model = model
        self.buy_price = buy_price
        self.description = description

