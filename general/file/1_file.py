f = open('test.txt', 'r+')
print(f.read())

'''
this is sample text for learning
this is second line
'''

print(f.read())
# empty

f.close()

f = open('test.txt', 'r+')
print(f.readline())

'''
this is sample text for learning
'''

print(f.readline())

'''
this is second line
'''

print(f.readline())
# empty

print(f.readline())
# empty

f.close()

f = open('test.txt', 'r+')
for line in f:
    print(line, end='')

'''
this is sample text for learning
this is second line
'''

f.close()

f = open('test.txt', 'r+')
print(list(f))

'''
['this is sample text for learning\n', 'this is second line\n']
'''

print(f.readlines())
# []

f.close()

f = open('test.txt', 'r+')
print(f.readlines())

'''
['this is sample text for learning\n', 'this is second line\n']
'''


print(f.write("writing into file\n"))
f.close()

f = open('test.txt', 'r+')
print(f.readlines())

'''
['this is sample text for learning\n', 'this is second line\n', 'writing into file\n']
'''


l = [1,2,3]
print(str(l))
# '[1, 2, 3]'

f = open('test.txt', 'r+')
print(f.write(str(l)))
# 9
f.close()


f = open('test.txt', 'r+')
print(f)

print(f.write('123'))
# 3

print(f.seek(10))
# 10

'''
pending update below
>>> f.write('123')
3
>>> f.read(1)
's'
>>> f.seek(-2,2)
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    f.seek(-2,2)
io.UnsupportedOperation: can't do nonzero end-relative seeks
>>> f.seek(3,2)
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    f.seek(3,2)
io.UnsupportedOperation: can't do nonzero end-relative seeks
>>> f.seek(-3, 2)
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    f.seek(-3, 2)
io.UnsupportedOperation: can't do nonzero end-relative seeks
>>> f.seek(1)
1
>>> f.read(1)
'2'
>>> f.close()
>>> f.closed
True
>>> f = open('test.txt', 'r+')
>>> f.closed
False
>>> f.tell()
0
>>> f.seek(1)
1
>>> f.tell()
1
>>> f.seek(5)
5
>>> f.tell()
5
>>> f.close()
>>>'''
