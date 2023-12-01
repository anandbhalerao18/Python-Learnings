# Magic / dunder methods in python
class employee:
    def __init__(self, name):
        self.name = name 
    name = "Anand"
    def __len__(self):
        i = 0 
        for c in self.name:
            i = i + 1 
        return i
            

e = employee()
# print(e.name)
# print(len(e))