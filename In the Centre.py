def is_central(txt):
    non_space_char_index = txt.index(next(filter(str.strip, txt)))
    return non_space_char_index == len(txt) - non_space_char_index - 1
