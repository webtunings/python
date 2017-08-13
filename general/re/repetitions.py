import re
str = "aabbbbababababaaaaabbbbbaabbaaabbb"
matches = re.findall(r'a{2}',str)
print(matches)
#['aa', 'aa', 'aa', 'aa', 'aa']
matches = re.findall(r'a{3}',str)
print(matches)
#['aaa', 'aaa']
matches = re.findall(r'a{4}',str)
print(matches)
#['aaaa']
matches = re.findall(r'a{5}',str)
print(matches)
#['aaaaa']
matches = re.findall(r'a{6}',str)
print(matches)
#[]

matches = re.findall(r'b{2}',str)
print(matches)
#['bb', 'bb', 'bb', 'bb', 'bb', 'bb']
matches = re.findall(r'b{3}',str)
print(matches)
#['bbb', 'bbb', 'bbb']
matches = re.findall(r'b{4}',str)
print(matches)
#['bbbb', 'bbbb']
matches = re.findall(r'b{5}',str)
print(matches)
#['bbbbb']
matches = re.findall(r'b{6}',str)
print(matches)
#[]

matches = re.findall(r'a{2,3}',str)
print(matches)
#['aa', 'aaa', 'aa', 'aa', 'aaa']

matches = re.findall(r'a{2,4}',str)
print(matches)
#['aa', 'aaaa', 'aa', 'aaa']

matches = re.findall(r'a{2,5}',str)
print(matches)
#['aa', 'aaaaa', 'aa', 'aaa']
