class Storage:
    def __init__(self, stuff, count):
        self.id = None
        self.stuff = stuff
        self.count = count
    def __repr__(self):
        return  str(self.__dict__)