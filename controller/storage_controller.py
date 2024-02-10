from model.da.storage_da import StorageDa
from model.entity.storage import Storage
from validators.validator import name_validator
import tkinter.messagebox as msg

class StorageController:



    def save(self,stuff, count):
        try:
            storage = storage(name_validator(stuff , "invalid stuff"), count)
            da = StorageDa()
            result = da.save(storage)
              if result:
                  return f"{storage} saved"
        except Exception as e:
            print(e)

    def edit(self, id , stuff , count):
        try:
            da = StorageDa()
            storage = da.find_by_id(storage , id)
            if storage:
                storage.stuff = name_validator(stuff, "invalid stuff")
                storage.count = count
                da.edit(storage)
                return f"storage {id} edited"
        except Exception as e:
            print(e)


    def remove_by_id(self, id):
        try:
            da = StorageDa()
            da.remove_by_id(storage, id)
            return f"storage {id} has been removed"

        except Exception as e:
            print(e)


      def find_by_id(self, id):
        try:
            da = storageDa()
            medical = da.find_by_id(storage, id)
            print(storage)
            if storage:
                return f"find storage by id {id}"
        except Exception as e:
            print(e)
    

    
    def find_by_stuff(self, stuff):
        try:
            if name_validator(stuff, "invalid stuff"):
                da = StorageDa()
                result = da.find_by_stuff(stuff)
                if result:
                    return f"storage {stuff} found"
        except Exception as e:
            print(e)


    def find_by_count(self, count):
        try:
            da = StorageDa()
            result = da.find_by_count(count)
            if result:
                return f"storage {count} found"
        except Exception as e:
            print(e)

