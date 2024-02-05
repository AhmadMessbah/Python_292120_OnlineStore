from model.da.database_manager import DatabaseManager
from model.entity.stuff import Stuff

class StuffDa(DatabaseManager):
    pass


    def find_by_name(self, name):
        self.make_engine()
        entity = self.session.query(Stuff).filter(Stuff.name == name).all()
        return entity.first()

    def find_by_name(self, brand):
        self.make_engine()
        entity = self.session.query(Stuff).filter(Stuff.brand == brand).all()
        return entity.first()

    def find_by_name(self, model):
        self.make_engine()
        entity = self.session.query(Stuff).filter(Stuff.model == model).all()
        return entity.first()