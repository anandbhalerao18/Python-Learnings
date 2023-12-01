a = "anand!!!!!!!!!!!" # strings are inmutable
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("anand", "john"))

b = "!!!anand!!!!"
print(b.rstrip("!"))

c = "anand,anand,anand,anand,anand"
print(c.replace("anand", "bhai"))
print(c.count("anand"))

d = "anand bhalero is a good boy and has roll no 456"
print(d.split(" "))

e = "this is my new car"
ee = "this is MY NEW car"
print(e.capitalize())
print(ee.capitalize())  # here we understand that capitalize turns only first letter capital and others to small letters 


f = "welcome to the console !!!"
print(f.center(50))
print(len(f.center(50)))
print(len(f))

g = "welcome to the console !!!"
print(g.endswith("!!!"))

f = "welcome to my console !!! "
print(f.endswith("to", 4, 10))

str2 = "he's name is dan. he is an honest man."
print(str2.find("is"))
# print(str2.find("ishhh"))
# print(str2.index("ishhh")) # it will pop up an error

r = "WelcomeTOTHeConsole"
print(r.isalpha()) 
ii = "Welcome00"
print(ii.isalpha())

y = "HELLOWORLD"
print(y.lower())

nn = "w wuish you a happy birthday "
print(nn.isprintable())
nnn = "today is my birthday \n"
print(nnn.isprintable())
nnnn = "                        "  # it will return true even it has space between 
print(nnnn.isprintable())

yyy = "This is my title"
yyyyy = "World Health Organisation"
print(yyy.istitle())
print(yyyyy.istitle())
print(yyy.isupper)


zz = "Python is a Interpreted Language"
print(zz.startswith("Python"))
print(zz.startswith("javascript"))
print(zz.swapcase())
print(zz.title())
