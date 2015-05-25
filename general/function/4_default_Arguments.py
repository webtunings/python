>>> def test(a, b=5, c=100):
	print("a=",a)
	print("b=",b)
	print("c=",c)

	
>>> test()
Traceback (most recent call last):
  File "<pyshell#422>", line 1, in <module>
    test()
TypeError: test() missing 1 required positional argument: 'a'
>>> test(1)
a= 1
b= 5
c= 100
>>> test(1,2)
a= 1
b= 2
c= 100
>>> test(1,2,3)
a= 1
b= 2
c= 3
