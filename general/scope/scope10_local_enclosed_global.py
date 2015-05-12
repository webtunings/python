>>> x = "global"
>>> def test():
	def inner():
		print(x)
	inner()

	
>>> x
'global'
>>> test()
global
>>> def test():
	x = "enclosed"
	def inner():
		print(x)
	inner()

	
>>> x
'global'
>>> test()
enclosed
>>> def test():
	x = "enclosed"
	def inner():
		x = "inner"
		print(x)
	inner()

	
>>> x
'global'
>>> test()
inner
