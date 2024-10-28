def map_letters(word):
    letter_map = {}
    
    for index, letter in enumerate(word):
        if letter in letter_map:
            letter_map[letter].append(index)
        else:
            letter_map[letter] = [index]
    
    return letter_map