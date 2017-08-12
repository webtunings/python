import re
str = "nlkjfdnosueirhfweanfsdkvfns;dknkwa"
value = re.split(r'[a-f]',str)
print(value)
#['nlkj', '', 'nosu', 'irh', 'w', '', 'n', 's', 'kv', 'ns;', 'knkw', '']

match = re.search(r'[a-f]',str)
print(match.group())
#f

matches = re.findall(r'[a-f]',str)
print(matches)
#['f', 'd', 'e', 'f', 'e', 'a', 'f', 'd', 'f', 'd', 'a']
print(len(matches))
#11

