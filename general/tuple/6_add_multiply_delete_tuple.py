>>> t1 = (1,2,3)
>>> t2 = (4,5,6)
>>> t3 = t1 + t2
>>> t3
(1, 2, 3, 4, 5, 6)
>>> t1 * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> del t1[0]
Traceback (most recent call last):
  File "<pyshell#1121>", line 1, in <module>
    del t1[0]
TypeError: 'tuple' object doesn't support item deletion
>>> del t1
>>> t1
Traceback (most recent call last):
  File "<pyshell#1123>", line 1, in <module>
    t1
NameError: name 't1' is not defined
>>> 
