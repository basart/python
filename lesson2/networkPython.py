import urllib2
u = urllib2.urlopen('http://www.google.by/?q=Python')
print u.getcode()

print u.msg
print u.read()