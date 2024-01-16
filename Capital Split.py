def cap_space(txt):
    return ''.join(' ' + char if char.isupper() else char for char in txt).lower()