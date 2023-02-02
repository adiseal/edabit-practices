def word_lengths(lst):
    word_lengths = []
    for x in lst:
        word_lengths.append(len(x))
    return word_lengths
    
assert word_lengths(["hello", "world"]) == [5, 5]
