a = ['my', 'name', 'is', 'praveen']
print('****'.join(a))
# my****name****is****praveen
print(' '.join(a))
# my name is praveen

#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    list_splitted = line.split(" ")
    string_joined = "-".join(list_splitted)
    return string_joined

print(split_and_join("your name is richa"))