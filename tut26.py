letter = "hey my name is {} and I am from {}"
country = "India"
name = "Anand"
# print(letter.format(name, country))
letter = "hey my name is {1} and I am from {0}"
print(letter.format(country, name))


# F-string
print(f"we use fstrings like this : hey my name is {name} and I am from {country}")
print(f"we use fstrings like this : hey my name is {{name}} and I am from {{country}}")
