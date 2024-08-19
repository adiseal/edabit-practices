import re

def get_name(email):
    # Extract the part before the @ symbol
    name_part = email.split('@')[0]
    # Use a regex to keep only alphabetical characters
    name = re.sub(r'[^a-zA-Z]', '', name_part)
    return name