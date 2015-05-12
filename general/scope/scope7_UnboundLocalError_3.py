>>> a = 10
>>> def test(b):
	if b == 5:
		print(a)
	def a(x):
		return x
	print(a)

	
>>> test(3)
<function test.<locals>.a at 0x0000000002D76EA0>
>>> test(5)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    test(5)
  File "<pyshell#12>", line 3, in test
    print(a)
UnboundLocalError: local variable 'a' referenced before assignment
