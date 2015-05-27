>>> l = [12,13,1,2,3,6]
>>> del l[1]
>>> l
[12, 1, 2, 3, 6]
>>> del l[0:2]
>>> l
[2, 3, 6]
>>> del l
>>> l
Traceback (most recent call last):
  File "<pyshell#839>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> 
