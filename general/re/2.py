>>> str = "email-new.user@gmail.com"
>>> match = re.search(r'\w+@\w+', str)
>>> match
<_sre.SRE_Match object at 0x2b3e8e400988>
>>> match.group()
'user@gmail'
>>> match = re.search(r'[\w.-]@[\w.-]', str)
>>> match.group()
'r@g'
>>> match = re.search(r'[\w.-]+@[\w.-]+', str)
>>> match.group()
'email-new.user@gmail.com'
>>> 

