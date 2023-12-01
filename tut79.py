# multiple inheritance in python
class employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")
class dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"The dance is {self.dance}")
    

class DancerEmployee(dancer, employee):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

o = DancerEmployee("hiphop", "shivaa")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())