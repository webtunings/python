>>> x = 10
>>> def test():
	print("x =", x)
	print(locals())
	print(globals())

	
>>> test()
x = 10
{}
{'__doc__': None, 'test': <function test at 0x000000000369DD90>, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__name__': '__main__', '__package__': None, '__builtins__': <module 'builtins' (built-in)>, 'x': 10}
