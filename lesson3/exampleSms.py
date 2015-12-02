#-*- coding:utf8 -*-
import urllib2
import urllib
api_key = 'e96f3c28-5e50-ff64-7d28-1af3e2129d3a'
phone = '+375447827450'
url_template = 'http://sms.ru/sms/send?api_id=%(api_key)s&to=%(phone)s'
url = url_template % {"api_key": api_key, "phone": phone}
text = u'Hello, Медвед!!'
encoded_text = urllib.urlencode({"text": text.encode('utf-8')})
print(encoded_text)
headers = {"Content-type": "application/x-www-form-urlencoded", }
r = urllib2.Request(url, data=encoded_text, headers=headers)
u = urllib2.urlopen(r)
print(u.read())

