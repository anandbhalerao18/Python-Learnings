# super keyword in python
# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method")

# class ChildClass(ParentClass):
#     def child_method(self):
#         print("This is the child method")
#         super().parent_method()

# child_Object = ChildClass()
# child_Object.child_method()



class Employee:
    def __init__(self, Name, id):
        self.name = Name
        self.id = id

class programmer:
    def __init__(self, name, id, lang):
        self.name = name
        self.id = id
        self.lang = lang

rohit = Employee("Rohit sharma", "90")
Virat = programmer("virat kolhi", "60", "Python")

print()
