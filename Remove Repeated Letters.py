def remove_repeats(word):
    result = ""
    for i in range(len(word)):
        if i == 0 or word[i] != word[i-1]:
            result += word[i]
    return result