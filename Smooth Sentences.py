def is_smooth(sentence):
    words = sentence.split()
    for i in range(len(words) - 1):
        if words[i].lower()[-1] != words[i+1].lower()[0]:
            return False
    return True
