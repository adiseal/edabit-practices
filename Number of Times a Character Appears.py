def char_appears(sentence, char):
    sentence = sentence.lower()
    char = char.lower()
    
    words = sentence.split()
    
    return [word.count(char) for word in words]

