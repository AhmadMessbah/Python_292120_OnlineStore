from model.da.transaction_da import TransactionDa
from model.entity.transaction import Transaction
from validators.validator import date_validator
import tkinter.messagebox as msg
from model.da.payment_da import Payment

class TransactionController:
    def save(self,usernsme , stuff, quantity, total_price ,date_time, status=True):
        try:
            transaction = Transaction(username_validator(username, "invalid username"), 
                          name_validator(stuff, "invalid stuff"),
                          date_validator(date_time, "invalid date_time"),
                transaction = Transaction(date=date_time)
                da = TransactionDa()
                result = da.save(transaction)
            except Exception as e:
                 e.with_traceback()
                 return e


    def remove_by_id(self, id):
        try:
            da = TransactionDa()
            result = da.remove_by_id(transaction , id)
            return f"Transaction has been removed by id {id}"

        except Exception as e :
            return e


    def find_by_id(self, id):
        try:
            da = TransactionDa()
            result = da.find_by_id(transaction, id )
            if result:
                return f"transaction found by id {id}"

        except Exception as e:
            return e

    def find_by_username(self, username):
        try:
           da = TransactionDa()
           result = da.find_by_user(transaction , username)
           if result:
              return f"Transaction found by username {username}"

        except Exception as e:
            return e

    def find_by_date_time(self, date_time):
        try:
            if date_validator(date , "error"):
               da = TransactionDa()
               result = da.find_date_time(date_time)
               msg.showinfo("info", str(result))
                
               return "Transaction found by date_time {date_time}"

        except Exception as e:
            msg.showerror("error",f"error : {e}")


    def change_quantity_of_stuff(self,quantity,stuff):
        transaction = Transaction.get(id)

        if transaction and transaction.status == "pending":

        Stuff = stuff.objects.get(id=stuff)

        if quantity > 0 and quantity <= stuff.available_quantity:

            stuff.available_quantity -= quantity
            stuff.save()

            transaction.status = "completed"
            transaction.save()

            return "Transaction completed successfully"
        else:

            return "Invalid quantity"

total_price = sum(bu)
print('Total price is',total_price)

