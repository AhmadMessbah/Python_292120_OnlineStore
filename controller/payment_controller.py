from model.da.payment_da import PaymentDa
from model.entity.payment import Payment
from model.tools.validation import name_validator and family_validator
import tkinter.messagebox as msg

class UserController:



    def save(self,name,model,buy_price,description, status=True):
        try:
            payment = Payment(id,name,model,buy_price,description)
            da = PaymentDa()
            da.save(payment)
            return "User saved"
        except Exception :
            return "Error saving"


    def edit(self,name,model,buy_price,description ):
        try:
            payment = Payment(id,name,model,buy_price,description)
            da = PaymentDa()
            da.save(Payment)
            return "Payment edit"
        except Exception :
            return "Error saving"


    def remove(self, id):
        try:
            da = PaymentDa()
            da.remove(id)
            return "Payment has been removed"

        except Exception :
            return "Error while"

    def find_all(self):
        try:
            da = PaymentDa()
            da.find_all(id)
            return "payment found"

        except Exception :
            return "Error finding"


    def find_by_name(self, name):
        try:
           da = PaymentDa()
           da.find_by_name(name)
           return "person found by name"

        except Exception :
            return "Error while"


    def find_by_model(self,model):
        try:
            da = PaymentDa()
            da.find_by_model(model)
            return "Payment found"
        except Exception :
            return "Error while"

    def find_by_buy_price(self, buy_price):
        try:
            da = PaymentDa()
            da.find_by_model(buy_price)
            return "buy price found"
        except Exception :
            return "Error while"
