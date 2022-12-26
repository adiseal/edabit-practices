def has_key(dictionary, key):
    is_exists = key in dictionary.keys()
    return is_exists

    
assert has_key({ "a": 44, "b": 45, "c": 46 }, "d") == False

assert has_key({ "craves": True, "midnight": True, "snack": True }, "morning") == False

assert has_key({ "pot": 1, "tot": 2, "not": 3 }, "not") == True