import re
pattern = '\w+'
text = 'abc def'

for match_object in re.finditer(pattern, text):
    start = match_object.start()
    end = match_object.end()
    print('matched string = ', text[start:end], ' start = ', start, ' end = ', end)

#matched string =  abc  start =  0  end =  3
#matched string =  def  start =  4  end =  7

