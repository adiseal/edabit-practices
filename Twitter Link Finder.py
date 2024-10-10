import re

def tweet(text):
    pattern = r"[@#]\w+"
    return ' '.join(re.findall(pattern, text))