from model.da.user_da import UserDa
from model.entity.user import User
from model.tools.validation import name_validator
import tkinter.messagebox as msg

class UserController:



    def save(self,  name, family, username, password, role, status=True):
        try:
            user = User(id, name, family, username, password, role,status)
            da = UserDa()
            da.save(user)
            return "User saved"
        except Exception as e:
            return "Error saving"


    def edit(self,  id, name, family, username, password, role ):
        try:
            user = User(id, name, family, username, password, role)
            da = UserDa()
            da.save(user)
            return "User edit"
        except Exception as e:
            return "Error saving"


    def remove(self, id):
        try:
            da = UserDa()
            da.remove(id)
            return "person has been removed"

        except Exception as e:
            return "Error while"

    def find_all(self):
        try:
            da = UserDa()
            da.find_all(id)
            return "person found"

        except Exception as e:
            return "Error finding"


    def find_by_username(self, username):
        try:
           da = UserDa()
           da.find_by_username(username)
           return "person found by username"

        except Exception as e:
            return "Error while"


    def find_by_username_and_password(self, username, password):
        try:
            da = UserDa()
            da.find_by_username_and_password(username, password)
            return "person found by username and password"

        except Exception as e:
            return "Error while"

        class UserController:
            pass
