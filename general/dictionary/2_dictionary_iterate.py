>>> d = {'x': 1000, 'y': [1,2,3], 'z': (1,2,3)}
>>> d
{'y': [1, 2, 3], 'x': 1000, 'z': (1, 2, 3)}
>>> d.items()
dict_items([('y', [1, 2, 3]), ('x', 1000), ('z', (1, 2, 3))])
>>> for key, value in d.items():
	print("key= ", key)
	print("value= ", value)

	
key=  y
value=  [1, 2, 3]
key=  x
value=  1000
key=  z
value=  (1, 2, 3)
