# raising custum errors 
a = int(input("Enter any number between 5 to 9 - "))
if (a<5 or a>9):
    raise ValueError("Value should be between 5 to 9 ")