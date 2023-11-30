def shared_letters(word1, word2):
    # Convert the words to sets of unique characters
    set1 = set(word1)
    set2 = set(word2)

    # Find the intersection of the two sets
    shared = set1.intersection(set2)

    # Return the number of shared characters
    return len(shared)