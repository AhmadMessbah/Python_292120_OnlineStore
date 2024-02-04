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

    def edit(self,user, stuff, quantity, total_price ,date_time, status):
        try:
            transaction = Transaction(id,user, stuff, quantity, total_price ,date_time, status)
            da = TransactionDa()
            da.save(Transaction)
            return "Transaction edit"
        except Exception as e:
            return "Error saving"


    def remove(self, id):
        try:
            da = TransactionDa()
            da.remove(id)
            return "Transaction has been removed"

        except Exception as e:
            return "Error while"

    def find_all(self):
        try:
            da = TransactionDa()
            da.find_all(id)
            return "Transaction found"

        except Exception as e:
            return "Error finding"


    def find_by_user(self, user):
        try:
           da = TransactionDa()
           da.find_by_user(user)
           return "Transaction found by user"

        except Exception as e:
            return "Error while"

    def find_by_user(self, date_time):
        try:
           da = TransactionDa()
           da.find_date_time(date_time)
           return "Transaction found by date/time"

        except Exception as e:
            return "Error while"

    def find_by_username_and_password(self,quantity):
        try:
            da = TransactionDa()
            da.find_by_quantity(quantity)
            return "Transaction found by quantity"

        except Exception as e:
            return "Error while"


