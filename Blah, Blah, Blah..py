def blah_blah(sentence, n):
    # Split the sentence into words
    words = sentence.split()

    # If n is greater than the number of words, replace all words with "blah"
    if n >= len(words):
        return ' '.join(['blah'] * len(words)) + "..."

    # Replace the last n words with "blah"
    words = words[:-n] + ['blah'] * n

    # Join the words back into a sentence, adding "..." at the end
    return ' '.join(words) + "..."