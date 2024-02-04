from model.da.stuff_da import StuffDa
from model.entity.stuff import Stuff
from model.tools.validation import name_validator
import tkinter.messagebox as msg

class StuffController:



    def save(self, name, brand, model, buy_price, description):
        try:
            stuff = Stuff(id, name, brand, model, buy_price, descriptions)
            da = StuffDa()
            da.save(stuff)
            return "Stuff saved"
        except Exception as e:
            return "Error saving"


    def edit(self,id, name, brand, model, buy_price, descriptions):
        try:
            stuff = Stuff(id, name, brand, model, buy_price, descriptions)
            da = StuffDa()
            da.save(stuff)
            return "Stuff edit"
        except Exception as e:
            return "Error saving"


    def remove(self, id):
        try:
            da = StuffDa()
            da.remove(id)
            return "Stuff has been removed"

        except Exception as e:
            return "Error while"

    def find_all(self):
        try:
            da = StuffDa()
            da.find_all(id)
            return "Stuff found"

        except Exception as e:
            return "Error finding"


    def find_by_name(self, name):
        try:
           da = StuffDa()
           da.find_by_username(name)
           return "Stuff found by name"

        except Exception as e:
            return "Error while"


    def find_by_brand(self,brand):
        try:
            da = StuffDa()
            da.find_by_brand(brand)
            return "person found by brand"

        except Exception as e:
            return "Error while"

    def find_by_brand(self, model):
        try:
            da = StuffDa()
            da.find_by_model(model)
            return "person found by model"

        except Exception as e:
            return "Error while"

