>>> def test():
	x = 5
	y = 10
	print(locals())
	print("x = ", x)
	print("y = ", y)

	
>>> test()
{'y': 10, 'x': 5}
x =  5
y =  10
>>> def test(z):
	x = 5
	y = 10
	print(locals())
	print("x = ", x)
	print("y = ", y)
	print("z = ", z)

	
>>> test(100)
{'y': 10, 'z': 100, 'x': 5}
x =  5
y =  10
z =  100
		
>>> def test(z):
	x = 5
	y = 10
	def inner():
		print("inner")
	print(locals())

	
>>> test(100)
{'inner': <function test.<locals>.inner at 0x0000000003661048>, 'y': 10, 'z': 100, 'x': 5}
>>> 
