>>> x = 10
>>> def test(y):
	if y < 5:
		x = 5
	print(x)

	
>>> test(1)
5
>>> test(20)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    test(20)
  File "<pyshell#5>", line 4, in test
    print(x)
UnboundLocalError: local variable 'x' referenced before assignment
