# how import works in python
import math
math.floor(4.2345)
math.sqrt(9)

from math import sqrt, pi
result = sqrt(9)*pi
print(result)

from math import sqrt as s
rec = s(9)*pi
print(rec)

import math as m
r = m.sqrt(9)* m.pi
print(r)

import math
print(dir(math))