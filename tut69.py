# class methods in python
class employee:
    company = "apple"
    def show(self):
        print(f"The number is {self.name} and company name is {self.company}")
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = employee()
e1.name = "Anand"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(employee.company)
