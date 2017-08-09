import re

str = "email-new.user@gmail.com"
match = re.search(r'\w+@\w+', str)
print(match)
#_sre.SRE_Match object at 0x2b3e8e400988>
print(match.group())
#'user@gmail'
match = re.search(r'[\w.-]@[\w.-]', str)
print(match.group())
#'r@g'
match = re.search(r'[\w.-]+@[\w.-]+', str)
print(match.group())
#'email-new.user@gmail.com'

