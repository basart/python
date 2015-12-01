import re

def find_message(text, message = ''):
    message = message.join(re.findall('[A-Z]', text))
    return message

encryption = find_message('How are you? Eh, ok. Low or Lower? Ohhh.')
print(encryption)
