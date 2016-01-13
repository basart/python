#-*- coding:utf8 -*-
import smtplib
import argparse

from email.message import Message
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_parse():
    parse = argparse.ArgumentParser()
    parse.add_argument('--email')
    parse.add_argument('--password')
    parse.add_argument('--email_recipient')
    parse.add_argument('--host')
    parse.add_argument('--port')
    parse.add_argument('--text')
    parse.add_argument('--header')

    return parse

def send_message(args_command_line):
    args = args_command_line.parse_args()
    msg = MIMEMultipart()
    #msg.set_charset('utf-8')
    msg['From'] = args.email
    msg['To'] = args.email_recipient
    header = Header(args.header)
    msg['Subject'] = header

    #text = args.text
    #msg.set_payload(args.text.decode('utf-8'), 'utf-8')
    msg.attach(MIMEText(args.text, 'plain'))
    smtp_obj = smtplib.SMTP(args.host, args.port)
    print(smtp_obj.starttls())
    print(smtp_obj.login(args.email, args.password))

    print(smtp_obj.sendmail(args.email, args.email_recipient, msg.as_string()))
    print(smtp_obj.quit())

if __name__ == "__main":
    parser = create_parse()
    send_message(parser)
