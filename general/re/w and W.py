>>> import re
>>> str = "test test123 test456"
>>> match = re.search(r'test\w\w\w', str)
>>> if match:
...  print "matched"
... else:
...  print "not matched"
... 
matched
>>> match.group()
'test123'
>>> match = re.search(r'test\W\W\W', str)
>>> if match:
...  print "matched"
... else:
...  print "not matched"
... 
not matched
>>> match.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
>>> 

