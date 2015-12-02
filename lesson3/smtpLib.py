import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_obj.ehlo())
print(smtp_obj.starttls())

print(smtp_obj.login('lets.python2015@gmail.com', 'nmKoAO1gFpGr7Kc'))
print(smtp_obj.sendmail('lets.python2015@gmail.com ', 'drednout.by@gmail.com', 'Subject: Hello.\n\nHello out of Python! How are you??:). Email Bot.'))
print(smtp_obj.quit())
