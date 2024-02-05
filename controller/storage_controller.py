from model.da.storage_da import StorageDa
from model.entity.storage import Storage
from model.tools.validation import name_validator
import tkinter.messagebox as msg

class StuffController:



    def save(self,stuff, count):
        try:
            stuff = Stuff(id,stuff, count)
            da = StuffDa()
            da.save(stuff)
            return "Stuff saved"
        except Exception as e:
            return "Error saving"


    def edit(self,id,stuff, count):
        try:
            storage = Storage(id,stuff, count)
            da = StorageDa()
            da.save(storage)
            return "storage edit"
        except Exception as e:
            return "Error saving"


    def remove(self, id):
        try:
            da = StorageDa()
            da.remove(id)
            return "Storage has been removed"

        except Exception as e:
            return "Error while"

    def find_all(self):
        try:
            da = StorageDa()
            da.find_all(id)
            return "storage found"

        except Exception as e:
            return "Error finding"


    def find_by_stuff(self, stuff):
        try:
           da = StorageDa()
           da.find_by_stuff(stuff)
           return "Storage found by stuff"

        except Exception as e:
            return "Error while"


    def find_by_brand(self,brand):
        try:
            da = StuffDa()
            da.find_by_brand(brand)
            return "person found by brand"

        except Exception as e:
            return "Error while"

