def sort_word(word):
    word = list(word)
    sorted = word.sort()
    final_word = ""
	
    for char in word:
        final_word = final_word + char
	
    return final_word
    
    
assert sort_word("dcba") == "abcd"

assert sort_word("Unpredictable") == "Uabcdeeilnprt"
# Capital letters should come first.

assert sort_word("pneumonoultramicroscopicsilicovolcanoconiosis") == "aacccccceiiiiiilllmmnnnnooooooooopprrsssstuuv"