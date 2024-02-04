from model.da.transaction_da import TransactionDa
from model.entity.transaction import Transaction
from model.tools.validation import name_validator
import tkinter.messagebox as msg

class TransactionController:
    def save(self,user, stuff, quantity, total_price ,date_time, status=True):
        try:
            if date_validator(date, "error"):
                timing = Transaction(date=date_time)
                da = TransactionDa()
                da.save(transaction)
                return " saved"
        except Exception as e:
            msg.showerror("error", f"error : {e}")

    def edit(self,user, stuff, quantity, total_price ,date_time, status):
        try:
            user = User(id,user, stuff, quantity, total_price ,date_time, status)
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
            da = UserDa()
            da.find_all(id)
            return "Transaction found"

        except Exception as e:
            return "Error finding"


    def find_by_username(self, username):
        try:
           da = UserDa()
           da.find_by_username(username)
           return "Transaction found by username"

        except Exception as e:
            return "Error while"


    def find_by_username_and_password(self, username, password):
        try:
            da = UserDa()
            da.find_by_username_and_password(username, password)
            return "Transaction found by username and password"

        except Exception as e:
            return "Error while"


