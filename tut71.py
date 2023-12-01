# dir, __dict__, and help method in python
x = [1,2,3]
print(dir(x))
print(x.__add__)



x = (1,2,3)
print(dir(x))
print(x.__add__)


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = person('honey', 45)
print(p.__dict__)


print(help(str))
print(help(person))