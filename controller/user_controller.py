from model.da.user_da import UserDa
from model.entity.user import User
from validators.validator import name_validator , family_validator , phone_validator , username_validator , password_validato


class UserController:
    def save(self,  name, family, username, password, phone, role , status=True):
        try:
            user = User(name_validator(name, "invalid name"), 
                        name_validator(family, "invalid family"),
                        username_validator(username, "invalid username"),
                        password_validator(password, "invalid password"),
                        phone_number_validator(phone_number, "invalid phone number"),
                        role
                        )
            print(user)
            da = UserDa()
            result = da.save(user)
        
        except Exception as e:
           if result:
                  return f"{user} saved"
        except Exception as e:
            print(e)


    def edit_by_user(self, id , name, family, username, password, phone , status=True ):
        try:
            da = UserDa()
            user = da.edit_by_user(user,id)
            if user:
                user.name = name_validator(name, "invalid name")
                user.family = family_validator(family, "invalid family")
                user.username = username_validator(username, "invalid username")
                user.password = password_validator(password, "invalid password")
                user.phone_number = phone_number_validator(phone_number, "invalid phone number")
                da.edit(user)
                return f"{user.name} {user.family} edit successful"
        except Exception e:
            return e


    def remove_by_id(self, id):
        try:
            da = UserDa()
            result = da.remove_by_id(user,id)
            if result:
                return f"person has been removed by id{id}"

        except Exception as e:
            return e

    def find_by_id(self, id):
        try:
            da = UserDa()
            result = da.find_by_id(user, id )
            if result:
                return f"person found by id {id}"

        except Exception as e:
            return e


    def find_by_username(self, username):
        try:
           if username_validator(username, "invalid username"):
           da = UserDa()
           result = da.find_by_username(user , username)
           if result:
               return f"person found by username {username}"

        except Exception as e :
            return e


   def find_by_phone(self, phone):
        try:
           if phonee_validator(phone, "invalid phone"):
           da = UserDa()
           result = da.find_by_phone(user , phone)
           if result:
               return f"person found by phone {phone}"

        except Exception as e :
            return e




    def find_by_username_and_password(self, username, password):
        try:
            if username_validator(username, "invalid username")and
               password_validator(password, "invalid password"):
            da = UserDa()
            result = da.find_by_username_and_password(username, password) ,
            if result:
                return f"person found by username and password {username}"

        except Exception as e :
            return e

    def find_by_name_and_family(self, name, family):
        try:
            if name_validator(name, "invalid name") and (family_validator(family, "invalid family"):
            da = UserDa()
            result = da.find_by_name_and_family(name, family)
            if result:
                return f"person found by name and family { name }{ family }"

        except Exception as e :
            return e
   


