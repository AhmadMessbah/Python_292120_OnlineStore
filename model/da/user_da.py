from model.da.database_manager import *
from model.entity.user import User


class UserDa(DatabaseManager):

    def find_by_username(self, username):
        self.make_engine()
        entity = self.session.query(User).filter(User.username == username).all()
        return entity.first()

    def find_by_username_and_password(self, username, password):
        self.make_engine()
        entity = self.session.query(User).filter(and_( User.username == username, User.password == password)).all()
        return entity.first()