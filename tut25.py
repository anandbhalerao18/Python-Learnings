tuple1 = (9,3,5,4,3,5,3,3,4,4,5,5,6,6,6,5,5,6,7,8,8,7,6,7,7,88,9999,65,90)
tem = tuple1.count(4) #it will show the number of 4s in the the tuple 1
# ress = tuple1.index(3) #it will show the serial number of 3 in tuple1
length = len(tuple1)
ress = tuple1.index(3, 6, 13) # it will slice in between the 6th digit and 13 digit and get the position of 3
print("The count of 4 in tuple1 is = ", tem)
print("The serial num of 3 in tuple1 is - ", ress)
print("The length of the tuple is - ", length)