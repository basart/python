import re
def find_message(text):
    list_simpole = re.findall('[A-Z]', text)
    message = ''
    for simbole in list_simpole:
        message += simbole
    return message

encryption = find_message( 'How are you? Eh, ok. Low or Lower? Ohhh.')
print(encryption)