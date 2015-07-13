
In [14]: pattern = "find me"

In [15]: text = "i am in between find me end"

In [16]: match = re.search(pattern, text)

In [17]: match.start()
Out[17]: 16

In [18]: match.end()
Out[18]: 23

In [19]: match.re
Out[19]: re.compile(r'find me', re.UNICODE)

In [20]: match.re.pattern
Out[20]: 'find me'

In [22]: match.string
Out[22]: 'i am in between find me end'

In [23]: print("found %s in %s from %d to %d match is %s" % (match.re.pattern, match.string, match.start(), match.end(), text[match.start():match.end()]))
found find me in i am in between find me end from 16 to 23 match is find me

