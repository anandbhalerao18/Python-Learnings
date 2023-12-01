#Enumarate Function in python 
marks = [55, 76, 87, 86, 85, 99, 8, 97, 4, 6]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Anand, is amazing")
#     index = index + 1


for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Anand, is amazing")
    index = index + 1

