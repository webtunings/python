import re
str = "email-new.user@gmail.com"
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
print(match.group())
#'email-new.user@gmail.com'
print(match.group(1))
#'email-new.user'
print(match.group(2))
#'gmail.com'

