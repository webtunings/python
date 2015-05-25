>>> x = 5
>>> def test(d = x):
	print(d)

	
>>> test()
5
>>> test(10)
10
>>> x = 40
>>> test()
5
>>> def test(data, l = []):
	l.append(data)
	return l

>>> test(1)
[1]
>>> test(2)
[1, 2]
>>> def test(data, l = None):
	if l is None:
		l = []
	l.append(data)
	return l

>>> test(1)
[1]
>>> test(2)
[2]
>>> test(3,[200,300])
[200, 300, 3]
>>> test(4)
[4]
