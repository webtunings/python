def fib(end):
    previous, next = 0, 1
    fibList = []
    while next < end:
        fibList.append(next)
        previous, next = next, next + previous
    return fibList


print(fib(20))
# [1, 1, 2, 3, 5, 8, 13]


print(fib(10))
# [1, 1, 2, 3, 5, 8]

