>>> l = [2,5,1,4,3,3,3,9]
>>> l.pop()
9
>>> l
[2, 5, 1, 4, 3, 3, 3]
>>> l.pop(0)
2
>>> l
[5, 1, 4, 3, 3, 3]
>>> l.clear()
>>> l
[]
>>> l = [2,5,1,4,3,3,3,9]
>>> l.index(5)
1
>>> l.index(3)
4
>>> l.index(10)
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    l.index(10)
ValueError: 10 is not in list
>>> l.count(3)
3
>>> l.count(9)
1
>>> l.sort()
>>> l
[1, 2, 3, 3, 3, 4, 5, 9]
>>> l.reverse()
>>> l
[9, 5, 4, 3, 3, 3, 2, 1]
>>> l.copy()
[9, 5, 4, 3, 3, 3, 2, 1]
>>> l
[9, 5, 4, 3, 3, 3, 2, 1]
>>> 
