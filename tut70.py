# class methods as alternative constructors
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = 12000


        @classmethod
        def fromstr(cls, string):
            return cls(string.split("-")[0],string.split("-")[1])

e1 = employee("anand", 12000)
print(e1.name)
print(e1.salary)


string = "oreo-90"
e2 = employee.fromStr(string)
print(e2.name)
print(e2.salary)
