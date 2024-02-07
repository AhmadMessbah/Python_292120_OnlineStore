from model.da.database_manager import *
from model.entity.payment import Payment

class PaymentDa(DatabaseManager):

    def find_by_name(self, name):
        self.make_engine()
        entity = self.session.query(Payment).filter(Payment.name == name).all()
        return entity.first()

    def find_by_model(self, model):
        self.make_engine()
        entity = self.session.query(Payment).filter(Payment.model == model).all()
        return entity.first()

    def find_by_buy_price(self, buy_price):
        self.make_engine()
        entity = self.session.query(Payment).filter(Payment.buy_price == buy_price).all()
        return entity.first()


   def find_payment_coumt_by_user_id(self, id):
        self.make_engine()
        entity = self.session.query(Payment).filter(Payment.id == id).all()
        return entity.first()
