# inheritance in python 
class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


    def showDetails(self):
        print(f'The name of employee: {self.id} is {self.name}')


class programmer(employee):
    def showLanguage(self):
        print("The default language is python ")


e1 = employee("rohit sharma", 599)
e1.showDetails()
e2 = programmer("virat kohli", 5799)
e2.showDetails()
e2.showLanguage()