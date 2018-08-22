d = {'x': [1, 2, 3], 'y': 123, 'z': "str"}
print(type(d))
# <class 'dict'>

print(d['x'])
# [1, 2, 3]

print(d['y'])
# 123

d['a'] = 100
print(d)
# {'y': 123, 'a': 100, 'x': [1, 2, 3], 'z': 'str'}

del d['a']
print(d)
# {'y': 123, 'x': [1, 2, 3], 'z': 'str'}

print(d.keys())
# dict_keys(['x', 'y', 'z'])

print(list(d.keys()))
# ['x', 'y', 'z']

print(sorted(d.keys()))
# ['x', 'y', 'z']


print('x' in d)
# True

print('a' in d)
# False

print('a' not in d)
# True

print('x' not in d)
# False


d = dict([('a', 100), ('b', 200)])
print(d)
# {'a': 100, 'b': 200}

print({x: x**3 for x in range(10)})
# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}

print({x: x**3 for x in (1, 2, 3)})
# {1: 1, 2: 8, 3: 27}

print({x: x**3 for x in [1, 2, 3]})
# {1: 1, 2: 8, 3: 27}

print(dict(a=100, b=200))
# {'a': 100, 'b': 200}

d.clear()
print(d)
# {}
