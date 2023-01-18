def get_word(left, right):
    sentence = left + right
    return sentence.title()
    
    
assert get_word("seas", "onal") == "Seasonal"

assert get_word("comp", "lete") == "Complete"

assert get_word("lang", "uage") == "Language"