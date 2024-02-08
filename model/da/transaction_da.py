from model.da.database_manager import DatabaseManager
from model.entity.transaction import Transaction
from model.da.payment_da import Payment


class TransactionDa(DatabaseManager):
    def find_by_date(self, date):
        self.make_engine()
        entity = self.session.query(Transaction).filter_by(date=date)
        return entity

    def find_by_user(self, user):
        self.make_engine()
        entity = self.session.query(Transaction).filter_by(user=user)
        return entity


    def find_by_quantity(self, quantity):
        self.make_engine()
        entity = self.session.query(Transaction).filter_by(quantity=quantity)
        return entity


    def find_by_stuff(self, stuff):
        self.make_engine()
        entity = self.session.query(Transaction).filter_by(stuff=stuff)
        return entity


    def find_by_quantity_of_stuff(self,quantity,stuff):
        self.make_engine()
        entity = self.session.query(Transaction).filter( Transaction.quantity == quantity, Transaction.stuff == stuff).all()
        return entity.first()


    def find_all(self):
        pass