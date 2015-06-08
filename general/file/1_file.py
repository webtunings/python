>>> f = open('test.txt', 'r+')
>>> f.read()
'this is a sample file\nfor the learning'
>>> f.read()
''
>>> f.close()
>>> f = open('test.txt', 'r+')
>>> f.readline()
'this is a sample file\n'
>>> f.readline()
'for the learning'
>>> f.readline()
''
>>> f.readline()
''
>>> f.close()
>>> f = open('test.txt', 'r+')
>>> for line in f:
	print(line, end='')

	
this is a sample file
for the learning
>>> f.close()
>>> f = open('test.txt', 'r+')
>>> for line in f:
	print(line)

	
this is a sample file

for the learning
>>> f.close()
>>> f = open('test.txt', 'r+')
>>> list(f)
['this is a sample file\n', 'for the learning']
>>> f.readlines()
[]
>>> f.close()
>>> f = open('test.txt', 'r+')
>>> f.readlines()
['this is a sample file\n', 'for the learning']
>>> f.write("writing into file")
17
>>> f.close()
>>> l = [1,2,3]
>>> str(l)
'[1, 2, 3]'
>>> f = open('test.txt', 'r+')
>>> f.write(l)
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    f.write(l)
TypeError: must be str, not list
>>> f.write(str(l))
9
>>> f.close()
>>> 
>>> f = open('test.txt', 'r+')
>>> f
<_io.TextIOWrapper name='test.txt' mode='r+' encoding='cp1252'>
>>> f.write('123')
3
>>> f.seek(10)
10
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
>>> 
