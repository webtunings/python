>>> name = "praveen"
>>> name[0]
'p'
>>> name[4]
'e'
>>> name[-1]
'n'
>>> name[0:2]
'pr'
>>> name[0:-2]
'prave'
>>> name[:3]
'pra'
>>> name[0:3]
'pra'
>>> name[1:]
'raveen'
>>> name[0:]
'praveen'
>>> name[:]
'praveen'
>>> name[2:]
'aveen'
>>> name[2:200]
'aveen'
>>> name[0]
'p'
>>> name[0] = "n"
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    name[0] = "n"
TypeError: 'str' object does not support item assignment
>>> "n" + name[1:]
'nraveen'
>>> len(name)
7
