import re
patterns = ['test1', 'test2']

text = ''' this is a simple text 
test1
test2
'''

for pattern in patterns:
   if re.search(pattern, text):
      print("match found for", pattern)

#match found for test1
#match found for test2


