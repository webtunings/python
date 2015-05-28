>>> t = (12,13,14)
>>> for value in t:
	print(value)

	
12
13
14
>>> for pair in enumerate(t):
	print(pair)

	
(0, 12)
(1, 13)
(2, 14)
>>> for index, value in enumerate(t):
	print(index, value)

	
0 12
1 13
2 14
>>> l = [12,13,14]
>>> for index, value in enumerate(l):
	print(index, value)

	
0 12
1 13
2 14
