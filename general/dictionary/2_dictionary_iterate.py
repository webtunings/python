d = {'x': 1000, 'y': [1,2,3], 'z': (1,2,3)}
print(d)
# {'y': [1, 2, 3], 'x': 1000, 'z': (1, 2, 3)}
print(d.items())
# dict_items([('y', [1, 2, 3]), ('x', 1000), ('z', (1, 2, 3))])


for key, value in d.items():
    print("key= ", key)
    print("value= ", value)

'''	
key=  x
value=  1000
key=  y
value=  [1, 2, 3]
key=  z
value=  (1, 2, 3)'''
