import re
pattern = '\w+'
text = 'abc def'

print(re.findall(pattern,text))

for match_string in re.findall(pattern, text):
   print(match_string)

#abc
#def

