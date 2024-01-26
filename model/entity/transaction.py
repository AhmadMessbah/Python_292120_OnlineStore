class Transaction:
    def __init__(self, transaction_id, product, quantity, total_price, date):
        self.transaction_id = transaction_id
        self.product = product
        self.quantity = quantity
        self.date = date
        self.total_price = total_price
