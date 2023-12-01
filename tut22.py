# list in python
marks = [4, 3, 5, "Anand", True, 45, 76, 00, "abc", 6, 8 ,75, 700, 56]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4]) 

# print(marks[-3]) # negative index 
# print(marks[len(marks)-3]) # positive index
# print(marks[5-3]) #postive index
# print(marks[2]) #positive index


# if 7 in marks:
#     print("Yes 7 is there in the marks")
# else:
#     print("no")


# if "nand" in "anand":
#     print("yes its there")

# print(marks)
# print(marks[:])
# print(marks[1:])
# print(marks[:7])
# print(marks[2:])
# print(marks[3:])
# print(marks[1:3])
# print(marks[2:-1]) #negative index
# print(marks[2:4]) #positive index
# print(marks[1:8:2]) #


st = [i for i in range(4)] #this is list comprention
print(st)

xt = [i*i for i in range(8)] #this is list comprention
print(xt)

oot = [i*i for i in range(8)if i%2==0] #this is list comprention
print(oot)

