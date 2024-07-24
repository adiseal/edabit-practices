def three_letter_collection(s):
    if len(s) < 3:
        return []
    
    three_letter_words = [s[i:i+3] for i in range(len(s) - 2)]
    return sorted(three_letter_words)