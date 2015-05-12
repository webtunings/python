>>> x = 10
>>> def test():
	x +=5

	
>>> test()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    test()
  File "<pyshell#3>", line 2, in test
    x +=5
UnboundLocalError: local variable 'x' referenced before assignment
>>> print(x)
10
>>> def test():
	global x
	x +=5

	
>>> print(x)
10
>>> test()
>>> print(x)
15
