'''
prototype: copy objects without know the obj type.
'''
from prototype_ import PrototypeFactory

def main():
    PrototypeFactory.initialize()

    # concrete 1 object copy
    instance = PrototypeFactory.get_con1()
    print(instance.get_type())

    # concrete 2 object copy
    instance = PrototypeFactory.get_con2()
    print(instance.get_type())


if __name__ == "__main__":
    main()