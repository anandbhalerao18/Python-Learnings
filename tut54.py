# 'is' verses '==' in python

a = [1,2,3, 55]
b = [1,2,3, 55]
print(a is b) #it compares the exact location of the object in memory 
print(a == b) #it compares the value of the the object 



c = 4
d = "4"
print(c is d)
print(c == d)

e = 8
f = 8
print(e is f)
print(e == f)


g = None
h = None
print(g is h)
print(g is None)
print(g == h)