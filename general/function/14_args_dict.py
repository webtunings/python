def test(**args):
    print(args)
    print(args["x"])
    print(args["y"])
    for key, value in args.items():
        print("key = ", key)
        print("value = ", value)
    print(type(args))


test(x=6, y=10)

'''
{'y': 10, 'x': 6}
6
10
key =  y
value =  10
key =  x
value =  6
<class 'dict'>
'''