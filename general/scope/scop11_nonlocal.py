>>> x = "global"
>>> def test():
	x = "enclosed"
	print(x)
	def inner():
		nonlocal x
		x = "now local"
		print(x)
	inner()
	print(x)

	
>>> x
'global'
>>> test()
enclosed
now local
now local
