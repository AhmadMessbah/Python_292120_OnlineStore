from model.da.transaction_da import TransactionDa
from model.entity.stuff import Stuff
from model.entity.transaction import Transaction
from model.entity.user import User

user1= User( "name", "family", "username", "password", "phone")
stuff1 = Stuff( "name", "brand", "model", 1000, "description")

transaction = Transaction(user1,stuff1,2,2500)
da = TransactionDa()
da.save(transaction)

