import copy
from abc import abstractmethod

# prototype interface object
class Prototype:
    type  = None

    @abstractmethod
    def clone(self):
        pass

    def get_type(self):
        return self.type

# concrete prototype
class ConcretePrototype1(Prototype):
    def __init__(self):
        self.type = "Type1"

    def clone(self):
        return copy.copy(self)


class ConcretePrototype2(Prototype):
    def __init__(self):
        self.type = "Type2"

    def clone(self):
        return copy.copy(self)


# client object
class PrototypeFactory:
    con_1 = None
    con_2 = None

    # create the object type
    @staticmethod
    def initialize():
        PrototypeFactory.con_1 = ConcretePrototype1()
        PrototypeFactory.con_2 = ConcretePrototype1()
        
    
    # return the copy object
    @staticmethod
    def get_con1():
        return PrototypeFactory.con_1.clone()

    @staticmethod
    def get_con2():
        return PrototypeFactory.con_2.clone()