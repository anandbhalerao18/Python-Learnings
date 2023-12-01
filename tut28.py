# recursion in python
# factiorial(5) : 5*4*3*2*1
# factiorial(4) : 4*3*2*1
# factiorial(3) : 3*2*1
# factiorial(2) : 2*1
# factiorial(1) : 1
# factiorial(0) : 1
# factiorial(n) : n * factorial(n-1)


def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))

# que - make a code to print the fabonacci sequence 
# fabonacci series is :
# f0 =0 , f1 = 1, f2 is addition of f1 and f2
# the genral formula is -> fn = f(n-1) +f (n-2)
nacho = int(input("Enter the fabonacchi number you want to - "))
nnn = nacho-1
nnnn = nacho-2
minus = nnn-nnnn
print("The fabonacci of", nacho, "is - ",minus  )