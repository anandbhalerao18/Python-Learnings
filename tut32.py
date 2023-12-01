# set1 = {2,4,5,6,7}
# set2 = {5,6,7,9,7,6,9,88,454}
# print(set1, set2)
# print(set1.union(set2))
# set1.update(set2)
# set2.update(set1)

city = {"delhi","hydrabad","pune","mumbai"}
city2 = {"delhi","nagpur","agra","mumbai"}
# var = city.intersection_update(city2)
# print(var)
# var2 = city.symmetric_difference(city2)
# print(var2)
# var3 = city.difference(city2)
# print(var3)
print(city.isdisjoint(city2))
print(city.issuperset(city2))
print(city.issubset(city2))
# city.add("khamgaon")
# print(city)

# city.remove("delhi")
# city.remove("amravati") #it will thorow an error as amravati is not in the set
# city.discard("amravati") #it will not throw an error if we write discard 
# print(city)

# item = city.pop()
# print(city)
# print(item)
# del city # it delets the set 


