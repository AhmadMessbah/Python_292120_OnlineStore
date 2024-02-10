from model.da.database_manager import DatabaseManager
from model.entity.transaction import Transaction



class TransactionDa(DatabaseManager):
    def find_by_date_time(self, date_time):
        self.make_engine()
        result = self.session.query(Transaction).filter_by(date_time=date_time)
        return result

    def find_by_username(self, username):
        self.make_engine()
        result = self.session.query(Transaction).filter_by(username=username)
        return result


    def find_by_id(self, id):
        self.make_engine()
        result = self.session.query(Transaction).filter_by(id=id)
        return result


   def find_all(self, **kwargs):
        pass
