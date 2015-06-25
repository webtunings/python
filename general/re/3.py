>>> str = "email-new.user@gmail.com"
>>> match = re.search(r'([\w.-]+)@([\w.-]+)', str)
>>> match.group()
'email-new.user@gmail.com'
>>> match.group(1)
'email-new.user'
>>> match.group(2)
'gmail.com'
>>> 

