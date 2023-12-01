# construction in python 
class person:

    def __init__(self, n, o):
        print("I am a Person")
        self.name = n
        self.name = o

    name = "anand"
    occ = "devloper"

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("Anand", "Devloper")
b = person("Divya", "Employee")
a.info()
b.info()
# # print(a.name)
# a.name = "divya"
# a.occ = "Employee"
# a.info()