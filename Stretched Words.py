def unstretch(word):
    result = ""
    for i in range(len(word)):
        if i == len(word) - 1 or word[i] != word[i + 1]:
            result += word[i]
    return result