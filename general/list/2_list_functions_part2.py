l = [2,5,1,4,3,3,3,9]
print(l.pop())
9

print(l)
[2, 5, 1, 4, 3, 3, 3]
print(l.pop(0))
# 2
print(l)
# [5, 1, 4, 3, 3, 3]

print(l.clear())
print(l)
# []

l = [2,5,1,4,3,3,3,9]
print(l.index(5))
# 1

print(l.index(3))
# 4
'''
>>> l.index(10)
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    l.index(10)
ValueError: 10 is not in list'''

print(l.count(3))
# 3
print(l.count(9))
# 1

l.sort()
print(l)
# [1, 2, 3, 3, 3, 4, 5, 9]
l.reverse()
print(l)
# [9, 5, 4, 3, 3, 3, 2, 1]
l.copy()
# [9, 5, 4, 3, 3, 3, 2, 1]
print(l)
[9, 5, 4, 3, 3, 3, 2, 1]
