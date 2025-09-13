def is_phone_number(text):
    if len(text) != 12:  # Phone numbers 12 characters. if not = 12 it'll return false.
        return False
    for i in range(0, 3):  # The first three characters must be numbers.
        if not text[i].isdecimal():
            return False
    if text[3] != '-':  # The fourth character must be a dash.
        return False
    for i in range(4, 7): # The next three characters must be numbers.
        if not text[i].isdecimal():
            return False
    if text[7] != '-':  # The eighth character must be a dash.
        return False
    for i in range(8, 12):  # The next four characters must be numbers.
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?', is_phone_number('415-555-4242'))
print(is_phone_number('415-555-4242'))
print('Is Moshi moshi a phone number?', is_phone_number('Moshi moshi'))
print(is_phone_number('Moshi moshi'))


# to use regular expressions:
import re
def is_phone_number_regex(text):
    phone_number_regex = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return phone_number_regex.match(text) is not None
print('Is 415-555-4444 a phone number?', is_phone_number_regex('415-555-4444'))
print(is_phone_number_regex('415-555-4444'))