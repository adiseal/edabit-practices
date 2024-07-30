def longest_7segment_word(words):
    # Define the set of invalid characters
    invalid_chars = {'k', 'm', 'v', 'w', 'x'}
    
    # Filter out words that contain any invalid characters
    valid_words = [word for word in words if not any(char in invalid_chars for char in word)]
    
    # Find the longest word among the valid words
    longest_word = ''
    for word in valid_words:
        if len(word) > len(longest_word):
            longest_word = word
            
    return longest_word