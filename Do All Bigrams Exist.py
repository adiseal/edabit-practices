def can_find(bigrams, words):
    # Create a set of all bigrams for efficient lookup
    bigram_set = set(bigrams)
    
    # Check if each bigram exists in any of the words
    for bigram in bigram_set:
        found = any(bigram in word for word in words)
        if not found:
            return False
    
    return True