def count_adverbs(sentence):
    words = sentence.split()
    count = 0
    for word in words:
        # Remove punctuation
        word = ''.join(e for e in word if e.isalnum())
        if word.endswith('ly'):
            count += 1
    return count