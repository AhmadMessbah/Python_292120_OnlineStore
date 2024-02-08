from model.da.transaction_da import TransactionDa
from model.da.payment_da import PaymentDa
from model.da.storage_da import StorageDa
from model.da.user_da import UserDa
from model.da.stuff_da import StuffDa
from model.entity.stuff import Stuff
from model.entity.transaction import Transaction
from model.entity.user import User
from model.entity.storage import Storage
from model.entity.payment import Payment

user1= User( "name", "family", "username", "password", "phone")
stuff1 = Stuff( "name", "brand", "model", 1000, "description")

transaction = Transaction(user1,stuff1,2,2500)
da = TransactionDa()
da.save(transaction)

