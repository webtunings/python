l = [10,20,30,40,50,60]
l.append(70)
print(l)
# [10, 20, 30, 40, 50, 60, 70]

l[len(l):] = [80]
print(l)
# [10, 20, 30, 40, 50, 60, 70, 80]

l.extend([90,100])
print(l)
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

l.append([1,2])
print(l)
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, [1, 2]]

print(len(l))
# 11

l.insert(0,1)
print(l)
# [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, [1, 2]]

l.insert(2,2)
print(l)
# [1, 10, 2, 20, 30, 40, 50, 60, 70, 80, 90, 100, [1, 2]]

l.insert(len(l),1)
print(l)
# [1, 10, 2, 20, 30, 40, 50, 60, 70, 80, 90, 100, [1, 2], 1]
print(l.remove(1))
print(l)
# [10, 2, 20, 30, 40, 50, 60, 70, 80, 90, 100, [1, 2], 1]

l.remove(1)
print(l)
# [10, 2, 20, 30, 40, 50, 60, 70, 80, 90, 100, [1, 2]]

# l.remove(1)

'''Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    l.remove(1)
ValueError: list.remove(x): x not in list
>>> 
'''