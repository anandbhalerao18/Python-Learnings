# classes and objects in python
# class
class person:
    name = "Anand"
    ocupation = "software engginer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.ocupation}")

a = person()
b = person()
a.name = "shubham"
a.ocupation = "Accountant"


b.name = "Nitu"
b.ocupation = "HR"
# print(a.name, a.ocupation)
b.info()
a.info()