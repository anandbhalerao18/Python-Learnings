# oprator overloading in python
class vector:
    def __init__(self, i , j, k):
        self.i = i
        self.j = j
        self.k = k


    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
v = vector(3, 5, 6)
print(v)
v2 = vector(5, 66, 2)
print(v2)

print(v + v2)
