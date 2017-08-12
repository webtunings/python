import re
str = "a/bccc/def/tyu"
value = re.split('/',str)
print(value)
#['a', 'bccc', 'def', 'tyu']

#split with space
str = "a b bbbbbbbbbbbbbbbbbb fff      frf  eww"
value = re.split(r'\s',str)
print(value)
#['a', 'b', 'bbbbbbbbbbbbbbbbbb', 'fff', '', '', '', '', '', 'frf', '', 'eww']


#split with one or more spaces
value = re.split(r'\s+',str)
print(value)
['a', 'b', 'bbbbbbbbbbbbbbbbbb', 'fff', 'frf', 'eww']