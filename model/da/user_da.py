from model.da.database_manager import *
from model.entity.user import User


class UserDa(DatabaseManager):

    def find_by_username(self, username):
        self.make_engine()
        entity = self.session.query(User).filter(User.username == username).all()
        return result

    def find_by_username_and_password(self, username, password):
        self.make_engine()
        entity = self.session.query(User).filter( User.username == username, User.password == password)
        return result

    def find_by_name_and_family(self, name, family):
        self.make_engine()
        entity = self.session.query(User).filter( User.name == name, User.family == family)
        return result)

    def find_by_phone(self, phone):
        self.make_engine()
        entity = self.session.query(User).filter(User.phone == phone)
        return result

    def find_id(self, id):
        self.make_engine()
        result = self.session.query(User).filter(User.id == id)
        return result

    def find_all(self, **kwargs):
        pass
    
