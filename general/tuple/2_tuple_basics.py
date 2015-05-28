>>> t = 123, 234.345, "str", [1,2,3]
>>> t
(123, 234.345, 'str', [1, 2, 3])
>>> t = (123, 234.345, "str", [1,2,3])
>>> t
(123, 234.345, 'str', [1, 2, 3])
>>> t = (123, 234.345, "str", [1,2,3], (1,2,3))
>>> t
(123, 234.345, 'str', [1, 2, 3], (1, 2, 3))
>>> t[0]
123
>>> t[0] = 100
Traceback (most recent call last):
  File "<pyshell#901>", line 1, in <module>
    t[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> empty = ()
>>> len(empty)
0
>>> t = "just one",
>>> type(t)
<class 'tuple'>
>>> t = ("just one",)
>>> type(t)
<class 'tuple'>
>>> t = ("just one")
>>> type(t)
<class 'str'>
