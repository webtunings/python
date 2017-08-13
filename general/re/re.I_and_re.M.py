import re
str = "abc ABC"

matches = re.findall(r'[a-c]+',str)
print(matches)
#['abc']

matches = re.findall(r'[a-c]+',str,re.I)
print(matches)
#['abc', 'ABC']