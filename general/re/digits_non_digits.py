import re
str = "a234b4190ggg343dsfdretg 32 ef5"
matches = re.findall(r'\d', str)
print(matches)
#['2', '3', '4', '4', '1', '9', '0', '3', '4', '3', '3', '2', '5']
print("total digits %s"%len(matches))
#total digits 13


matches = re.findall(r'\D', str)
print(matches)
#['a', 'b', 'g', 'g', 'g', 'd', 's', 'f', 'd', 'r', 'e', 't', 'g', ' ', ' ', 'e', 'f']
print("total non digits %s"%len(matches))
#total non digits 17

print("total characters", len(str))
#total characters 30


matches = re.findall(r'\d+', str)
print(matches)
#['234', '4190', '343', '32', '5']

matches = re.findall(r'\D+', str)
print(matches)
#['a', 'b', 'ggg', 'dsfdretg ', ' ef']

matches = re.findall(r'\s', str)
print(matches)
#[' ', ' ']

matches = re.findall(r'\w', str)
print(matches)
#['a', '2', '3', '4', 'b', '4', '1', '9', '0', 'g', 'g', 'g', '3', '4', '3', 'd', 's', 'f', 'd', 'r', 'e', 't', 'g', '3', '2', 'e', 'f', '5']
print("total words %s"%len(matches))
#total words 28
