# tuples in python
tup = (2, 4, 6)
print(type(tup), tup)


tupi = (2) # it will show int 
print(type(tupi), tupi)

ttt = (1,2,3,4,5,56,6,7,7,8,89)
# ttt[0] = 90 #it will throw an error 
print(type(ttt), ttt)
print(ttt[0])
print(ttt[1])
print(ttt[2])
print(ttt[3])
print(ttt[4])
print(ttt[9])
print(ttt[-3]) # over all lenght minus 3 
# print(ttt[48]) # it will throw an error

if 56 in ttt:
    print("Yes 56 is present")

tutu = ttt[1:4]
print(tutu)