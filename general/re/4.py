
>>> str = "new-email.1@cisco.com test.123.456-1@gmail.com"
>>> import re
>>> matches = re.findall(r'[\w.-]+@[\w.-]+', str)
>>> matches
['new-email.1@cisco.com', 'test.123.456-1@gmail.com']
>>> 


