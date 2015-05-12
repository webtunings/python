>>> x = 10
>>> def test():
	print(x)
	x = 5

	
>>> test()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    test()
  File "<pyshell#4>", line 2, in test
    print(x)
UnboundLocalError: local variable 'x' referenced before assignment
>>> 
