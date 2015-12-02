#-*- coding:utf8 -*-
import smtplib
from email.message import Message
from email.header import Header

msg = Message()
msg.set_charset('utf-8')
h = Header(u"Привет, Медвед!".encode('utf-8'), 'utf-8')
msg['Subject'] = h
text = u"Юникод текст:)"
msg.set_payload(text.encode('utf-8'))
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)

print(smtp_obj.starttls())
print(smtp_obj.login('lets.python2015@gmail.com', 'nmKoAO1gFpGr7Kc'))

print(smtp_obj.sendmail('lets.python2015@gmail.com ', 'basov_av@tut.by', msg.as_string()))
print(smtp_obj.quit())

