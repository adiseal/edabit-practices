def detect_word(txt):
    string = ""
    for i in txt:
        if i.islower() ==  True:
            string = string + i
    return string
          
print(detect_word("UcUNFYGaFYFYGtNUH")) #➞ "cat"