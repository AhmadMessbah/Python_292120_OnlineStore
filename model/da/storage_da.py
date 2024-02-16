from model.da.database_manager import *
from model.entity.storage import Storage


class StorageDa(DatabaseManager):

     def find_by_id(self, id):
        self.make_engine()
        result = self.session.query(Storage).filter(Storage.id == id)
        return result


    
    def find_by_stuff(self, stuff):
        self.make_engine()
        result = self.session.query(Storage).filter(Storage.stuff == stuff)
        return result

    def find_by_count(self, count):
        self.make_engine()
        result = self.session.query(Storage).filter(Storage.count == count)
        return result


    def find_all(self, **kwargs):
        pass
