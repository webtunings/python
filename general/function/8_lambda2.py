>>> 
>>> def inc(n):
	return lambda x: x + n

>>> f = inc(5)
>>> f(10)
15
>>> inc(3)(50)
53
