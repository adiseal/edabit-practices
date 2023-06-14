def dictionary(initial_word, words):
    return [word for word in words if word.startswith(initial_word)]
    
print(dictionary("bu", ["button", "breakfast", "border"])) # ["button"]