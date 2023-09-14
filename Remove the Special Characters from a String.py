import re

def remove_special_characters(s):
    # The regex pattern to find all characters that are not a-z, A-Z, 0-9, -, _, or space
    pattern = r'[^a-zA-Z0-9-_ ]'
    # Use the sub() method to replace them with an empty string
    return re.sub(pattern, '', s)
