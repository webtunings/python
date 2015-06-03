>>> letters = {'a', 'b', 'b', 'c', 'd', 'a', 'e'}
>>> letters
{'b', 'c', 'd', 'e', 'a'}
>>> type(letters)
<class 'set'>
>>> 'a' in letters
True
>>> 'f' in letters
False
>>> x = {'a', 'b', 'b', 'c', 'd', 'a', 'e'}
>>> x
{'b', 'c', 'd', 'e', 'a'}
>>> y = {'a', 'b', 'f', 'g', 'h'}
>>> y
{'f', 'b', 'a', 'g', 'h'}
>>> x - y
{'c', 'd', 'e'}
>>> y - x
{'h', 'f', 'g'}
>>> x | y
{'h', 'c', 'd', 'f', 'a', 'b', 'e', 'g'}
>>> x & y
{'b', 'a'}
>>> x ^ y
{'h', 'c', 'd', 'f', 'g', 'e'}
>>> z = set('abcdeffffffaaa')
>>> z
{'c', 'd', 'f', 'a', 'b', 'e'}
