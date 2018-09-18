str = "a      bcd ef gh"
print(str.split())
#['a', 'bcd', 'ef', 'gh']
str = "a,      bcd, ef, gh"
print(str.split(","))

str = "alpha "
print(str.isalnum())
#False

str = "alpha"
print(str.isalnum())
#True

str = "alpha123"
print(str.isalnum())
#True

str = "alpha123"
print(str.isalpha())
#False

str = "alpha"
print(str.isalpha())
#True


str = "alpha"
print(str.isdigit())
#False

str = "123"
print(str.isdigit())
#True

str = "abc"
print(str.islower())
#True

str = 'abc'
print(str.isupper())
#False