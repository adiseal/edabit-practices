def no_yelling(sentence):
    # Strip any trailing whitespace from the sentence
    sentence = sentence.rstrip()
    
    # Check if the last character is a question mark or an exclamation mark
    if sentence.endswith('?'):
        # Replace multiple '?' at the end with a single '?'
        return sentence.rstrip('?') + '?'
    elif sentence.endswith('!'):
        # Replace multiple '!' at the end with a single '!'
        return sentence.rstrip('!') + '!'
    
    # If it doesn't end with multiple question or exclamation marks, return it unchanged
    return sentence