def make_word_riddle(word):
    # Split the word at 'in'
    prefix, suffix = word.lower().split('in')
    
    # Insert the prefix into the second position of the suffix
    riddle_word = suffix[0] + prefix + suffix[1:]
    
    # Return the result in all caps
    return riddle_word.upper()