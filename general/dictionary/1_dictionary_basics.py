d = {'x': [1,2,3], 'y': 123, 'z': "str"}
>>> type(d)
<class 'dict'>
>>> d['x']
[1, 2, 3]
>>> d['y']
123
>>> d['a'] = 100
>>> d
{'y': 123, 'a': 100, 'x': [1, 2, 3], 'z': 'str'}
>>> del d['a']
>>> d
{'y': 123, 'x': [1, 2, 3], 'z': 'str'}
>>> d.keys()
dict_keys(['y', 'x', 'z'])
>>> list(d.keys())
['y', 'x', 'z']
>>> sorted(d.keys())
['x', 'y', 'z']
>>> 'x' in d
True
>>> 'a' in d
False
>>> 'a' not in d
True
>>> 'x' not in d
False
>>> d = dict([('a', 100), ('b', 200)])
>>> d
{'a': 100, 'b': 200}
>>> {x: x**3 for x in range(10)}
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
>>> {x: x**3 for x in (1,2,3)}
{1: 1, 2: 8, 3: 27}
>>> {x: x**3 for x in [1,2,3]}
{1: 1, 2: 8, 3: 27}
>>> dict(a=100,b=200)
{'a': 100, 'b': 200}
>>> d.clear()
>>> d
{}
