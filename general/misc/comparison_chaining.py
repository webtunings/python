>>> a = 5
>>> b = 10
>>> c = 20
>>> a < b
True
>>> a < b and b < c
True
>>> a < b < c
True
>>> d = 10
>>> a < b
True
>>> a < b and b == c
False
>>> a < b and b == d
True
>>> a < b == c
False
>>> a < b == d
True
