# finally in python
def func1():
   try:
    l = [2,4,5,6,7,8]
    i = int(input("Enter the number of Index - "))
    print(l[i])
    return 1
   except:
    print("Some error occoured in the code")
    return 0
   finally:
    print("This finally will always execute")
    # print("This finally will always execute")

x = func1()
print(x)