import string

def alliteration_correct(sentence):
    # Remove punctuation from the sentence
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Split the sentence into words
    words = sentence.split()
    
    # Filter out words that are 3 characters or less
    long_words = [word for word in words if len(word) > 3]
    
    # If there are no long words, return True (since there's no rule being violated)
    if not long_words:
        return True
    
    # Check that all long words start with the same letter (case insensitive)
    first_letter = long_words[0][0].lower()
    return all(word[0].lower() == first_letter for word in long_words)
