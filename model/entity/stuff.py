class Stuff:
    def __init__(self, name, brand, model, buy_price, description):
        self.id = None
        self.name = name
        self.buy_price = buy_price
        self.model = model
        self.description = description
        self.brand = brand
class Stuff:
    def __init__(self, name, brand, model, buy_price, description):
        self.id = None
        self.name = name
        self.buy_price = buy_price
        self.model = model
        self.description = description
        self.brand = brand

    def __repr__(self):
        return  str(self.__dict__)