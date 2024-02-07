from model.da.database_manager import *
from model.entity.storage import Storage


class StorageDa(DatabaseManager):

    def find_by_stuff(self, stuff):
        self.make_engine()
        entity = self.session.query(Storage).filter(Storage.stuff == stuff).all()
        return entity.first()

    def find_by_count(self, count):
        self.make_engine()
        entity = self.session.query(Storage).filter(Storage.count == count).all()
        return entity.first()


   def remove(self, id):
        self.make_engine()
        entity = self.session.query(Storage).filter(Storage.id == id).all()
       if entity.firdt().count > 0 :
           entity.update([storage.count: entity.first().count - 1])
           self.session.comit()
        return entity.first()

