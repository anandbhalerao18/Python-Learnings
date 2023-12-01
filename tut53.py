# map , filter and reduce 

def cube(x):
    return x*x*x
print(cube(2))

l = [1,2,3,4,5,6,7]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))

newl = list(map(cube, l))
print(newl)



# FILTER 
def filter_func(a):
    return a>4
newnewl = list(filter(filter_func, l))
print(newnewl)