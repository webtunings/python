x = 5


def test(d=x):
    print(d)


test()
# 5

test(10)
# 10

x = 40
test()
# 5


def test(data, l=[]):
    l.append(data)
    return l


print(test(1))
# [1]

print(test(2))
# [1, 2]


def test(data, l=None):
    if l is None:
        l = []
    l.append(data)
    return l


print(test(1))
# [1]

print(test(2))
# [2]


print(test(3,[200,300]))
# [200, 300, 3]

print(test(4))
# [4]
