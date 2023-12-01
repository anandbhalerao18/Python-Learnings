# exception handaling and python try...except
a = input("Enter the number here : ")
print(f"The Multiplication Table of {a} is :- ")
try:
 for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Sorry some syntax error has happend in the code")

print("There is some lines of imp code")
print("The End of the code ")




