def check(dict_first, dict_second, key):
    if key in dict_first and key in dict_second:
        if dict_first[key] == dict_second[key]:
            return True
        else:
            return "Not the same"
    else:
        return "One's empty"
