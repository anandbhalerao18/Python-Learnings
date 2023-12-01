# file IO in python 

# f = open('myfile.txt', 'r')
# print(f)
# text = f.read()
# print(text)
# f.close()

f = open('myfile.txt', 'a')
f.write('hello world')
f.close()