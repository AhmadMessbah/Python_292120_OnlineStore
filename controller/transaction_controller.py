from model.da.transaction_da import TransactionDa
from model.entity.transaction import Transaction
from model.tools.validation import date_validator
import tkinter.messagebox as msg

class TransactionController:
    def save(self,user, stuff, quantity, total_price ,date_time, status=True):
        try:
            if date_validator(date_time, "error"):
                transaction = Transaction(date=date_time)
                da = TransactionDa()
                da.save(transaction)
                return " saved"
        except Exception as e:
            msg.showerror("error", f"error : {e}")

    def edit(self,user, stuff, quantity, total_price ):
        try:
            transaction = Transaction(id,user, stuff, quantity )
            da = TransactionDa()
            da.save(Transaction)
            return "Transaction edit"
        except Exception :
            return "Error saving"


    def remove(self, id):
        try:
            da = TransactionDa()
            da.remove(id)
            return "Transaction has been removed"

        except Exception :
            return "Error while"

    def find_all(self):
        try:
            da = TransactionDa()
            da.find_all(id)
            return "Transaction found"

        except Exception :
            return "Error finding"


    def find_by_user(self, user):
        try:
           da = TransactionDa()
           da.find_by_user(user)
           return "Transaction found by user"

        except Exception :
            return "Error while"

    def find_by_date_time(self, date_time):
        try:
           da = TransactionDa()
           da.find_date_time(date_time)
           return "Transaction found by date/time"

        except Exception :
            return "Error while"

    def find_by_quantity(self,quantity):
        try:
            da = TransactionDa()
            da.find_by_quantity(quantity)
            return "Transaction found by quantity"

        except Exception as e:
            return "Error while"

    def find_by_stuff(self,stuff):
        try:
            da = TransactionDa()
            da.find_by_stuff(stuff)
            return "Transaction found by stuff"

        except Exception :
            return "Error while"

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
        else:

        return "Invalid transaction"
total_price = sum(buy_prices)
print('Total price is',total_price)

