from model.da.database_manager import DatabaseManager
from model.entity.stuff import Stuff

class StuffDa(DatabaseManager):
    pass


    def find_by_name(self, name):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff.name == name).all()
        return result

    def find_by_brand(self, brand):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff.brand == brand).all()
        return result

    def find_by_model(self, model):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff.model == model).all()
        return result


    def find_by_id(self, id):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff.id == id).all()
        return result

    def find_all(self, **kwargs):
        pass
