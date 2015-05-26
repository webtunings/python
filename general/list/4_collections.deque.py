>>> from collections import deque
>>> q = deque[3,2,5,6]
Traceback (most recent call last):
  File "<pyshell#463>", line 1, in <module>
    q = deque[3,2,5,6]
TypeError: 'type' object is not subscriptable
>>> q = deque([3,2,5,6])
>>> q
deque([3, 2, 5, 6])
>>> q.append(9)
>>> q
deque([3, 2, 5, 6, 9])
>>> q.append(11)
>>> q
deque([3, 2, 5, 6, 9, 11])
>>> q.popleft()
3
>>> q
deque([2, 5, 6, 9, 11])
>>> q.popleft()
2
>>> q
deque([5, 6, 9, 11])
