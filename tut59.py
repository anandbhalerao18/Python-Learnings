# decorators in python 


def greet(fx):
    def mfx():
        print("good morning")

    print("good morning")
    fx()
    print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello world ")

def add(a, b):
    print(a+b)

# hello()