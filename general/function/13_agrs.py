def test(*args):
    print(args)
    print(type(args))


test(1, 2, 3, 4)

'''
(1, 2, 3, 4)
<class 'tuple'>
'''