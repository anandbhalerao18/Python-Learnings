# docstrings

def square(n):
    '''takes in a number n, returns the square of n''' #this is an doc string which shows the work of the function but it is not a comment
# and doc string is written write below the name of the function or it will now work
    print(n**2)
square(5)
print(square.__doc__) #doc strings are not ignored as the comments they can also print
