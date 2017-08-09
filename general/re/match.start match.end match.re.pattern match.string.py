import re
pattern = "find me"
text = "i am in between find me end"
match = re.search(pattern, text)
print(match.start())
#16

print(match.end())
#23

print(match.re)
#re.compile(r'find me', re.UNICODE)

print(match.re.pattern)
#'find me'

print(match.string)
#'i am in between find me end'

print("found %s in %s from %d to %d match is %s" % (match.re.pattern, match.string, match.start(), match.end(), text[match.start():match.end()]))
#found find me in i am in between find me end from 16 to 23 match is find me

