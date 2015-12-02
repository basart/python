import re

r = re.compile("^[a-zA-Z_]{4,10}$")
r.match('abc')
#print(r)
print(r.match('abcfsaf'))
print(r.match('abcfsaf*'))
print(r.match('abc_test'))

