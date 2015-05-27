>>> list(filter(lambda x: x < 0, range(-10,10)))
[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
>>> list(filter(lambda x: x % 2, range(-10,10)))
[-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]
>>> list(filter(lambda x: x % 3, range(-10,10)))
[-10, -8, -7, -5, -4, -2, -1, 1, 2, 4, 5, 7, 8]
>>> list(filter(lambda x: x % 1, range(-10,10)))
[]
