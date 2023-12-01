#access modifiers in pythonn
class Employee:
    def __init__(self):
        self.__name = "Anand"
        
a = Employee()
# a.name(a.__name) # cannot be accesed directly
# print(a._Employee.__name) # can be excessed indirectly this is because of name mangling
print(a.__dir__())








