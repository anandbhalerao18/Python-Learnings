# local and global variable in python


x = 4 # this is an global variable 
print(x)

def hello():
    x = 5 # this is an local variable 
    print(f"The local x is {x}")
    print("Hello Anand")

print(f"The global x is {x}")
hello()
print(f"The global x is {x}")



x = 7 # global variable 
def func():
    global x
    x = 4
    y = 5 #local variable
    print(y)

func()
print(x)
#print(y) # this will throw an error because is a local variable and is not accesable outside of the function 
