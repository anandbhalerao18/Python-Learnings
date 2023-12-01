# instance variables and class variable in python
class Employee:
    companyName = "Microsoft"
    def __init__(self, name):
        self.name = name
        self.raise_amount = 00.03
    def showDetails(self):
        print(f"The name of employee is {self.name} and the raise amount is {self.raise_amount} and the company name is {self.companyName}")

# Employee.showDetails(emp1)
emp1 = Employee("Anand")
emp1.raise_amount = 88
emp1.companyName = "Apple US"
emp1.showDetails()
emp2 = Employee("Rohit")
emp2.showDetails()
