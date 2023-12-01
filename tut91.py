# genrators in python
def my_genrator():
    for i in range(5):
        yield i


gen = my_genrator()
print(next(gen))
print(next(gen))
print(next(gen))