from model.da.stuff_da import StuffDa
from model.entity.stuff import Stuff
from validators.validator import name_validator
import tkinter.messagebox as msg

class StuffController:



    def save(self, name, brand, model, buy_price, description):
        try:
            stuff = Stuff(name_validator(brand, model, buy_price, descriptions)
            da = StuffDa()
            result = da.save(stuff)
            return "Stuff saved"
        except Exception as e:
            print(e)


    def edit(self,id, name, brand, model, buy_price, descriptions):
        try:
            stuff = Stuff(id, name, brand, model, buy_price, descriptions)
            da = StuffDa()
            da.save(stuff)
            return "Stuff edit"
        except Exception :
            return "Error saving"


    def remove_stuff_by_id(self, id):
        try:
            da = StuffDa()
            result = da.remove(stuff , id)
            if result :
               return f"Stuff has been removed by {id}"

        except Exception as e:
            return e

    
    def find_by_id(self, id):
        try:
            da = StuffDaDa()
            stuff = da.find_id(stuff, id)
            print(stuff)
            if stuff:
                return f"find stuff by id {id}"
        except Exception as e:
            print(e)


    def find_by_name(self, name):
        try:
           da = StuffDa()
           result = da.find_by_name(stuff , name)
           if result:
               return f"Stuff found by name {name}"

        except Exception as: e
            return e


    def find_by_brand(self, brand):
        try:
           da = StuffDa()
           result = da.find_by_brand(stuff , brand)
           if result:
               return f"Stuff found by brand {brand}"

        except Exception as: e
            return e

    def find_by_model(self, model):
        try:
           da = StuffDa()
           result = da.find_by_model(stuff , model)
           if result:
               return f"Stuff found by model {model}"

        except Exception as: e
            return e

