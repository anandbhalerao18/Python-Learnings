# hybrid and hierarchical inheritance in python
class BaseClass:
    pass
class Derived1(BaseClass):
    pass
class Derived2(BaseClass):
    pass
class Derived3(Derived1, Derived2):
    pass