def validate_spelling(txt):    
    words = txt.split()
    last_word = words[-1].lower().strip('.?!')
    spelled_word = ''.join([word.lower().strip('.') for word in words[:-1]])
    return spelled_word == last_word