# string slicing 
# names = "anand,shubham"
# print(len(names))
# print(names[0:5])

fruit = "mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[2:5])
print(fruit[0:-3]) # python hears add print(fruit[0:len(fruit)-3]) and gives the output here len(fruit) is equal to 5
print(fruit[0:len(fruit)-3]) 
print(fruit[:len(fruit)-3]) # if there is blank space no 0 or any number is added then it is considerd as 0
print(fruit[-1:len(fruit)-3]) #here python interpreter will add print(fruit[len(fruit)-1:len(fruit)-3]) that becomens 5-1:5-3 that is 4:2
print(fruit[len(fruit)-1:len(fruit)-3]) 
print(fruit[len(fruit)-3:len(fruit)-1]) 


# quick quiz:
nm = "harry"
print(nm[-4:-2]) 
