>>> x = [1,2,3]
>>> def test():
	x.append(4)

	
>>> print(x)
[1, 2, 3]
>>> test()
>>> print(x)
[1, 2, 3, 4]
>>> def test():
	x = [7,8,9]
	x.append(10)

	
>>> print(x)
[1, 2, 3, 4]
>>> test()
>>> print(x)
[1, 2, 3, 4]
>>> 
