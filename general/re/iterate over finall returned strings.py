In [28]: pattern = '\w+'

In [29]: text = 'abc def'

In [30]: for match_string in re.findall(pattern, text):
   ....:     print(match_string)
   ....:     
abc
def

