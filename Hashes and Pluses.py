def hash_plus_count(txt):
    return [txt.count("#"), txt.count("+")]
    
        
assert hash_plus_count("###+") == [3, 1]

assert hash_plus_count("##+++#") == [3, 3]

assert hash_plus_count("#+++#+#++#") == [4, 6]

