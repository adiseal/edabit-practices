import re

def insert_whitespace(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
