import re

def is_valid_phone_number(phone_number):
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    return bool(re.match(pattern, phone_number))
