def unrepeated(word):    
    unique_chars = ""    
    for char in word:
        if char not in unique_chars:
            unique_chars += char    
    return unique_chars