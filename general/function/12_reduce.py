>>> from functools import reduce
>>> reduce
<built-in function reduce>
>>> reduce(lambda: a, b: a * b, [3,4,2,7])
SyntaxError: invalid syntax
>>> reduce(lambda a, b: a * b, [3,4,2,7])
168
>>> reduce(lambda a, b: a + b, [3,4,2,7])
16
>>> reduce(lambda a, b: a + 2 * b, [3,4,2,7])
29
