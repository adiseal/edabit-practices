def unique_abbrev(abbreviations, words):
    for abbrev in abbreviations:
        count = 0
        for word in words:
            if word.startswith(abbrev):
                count += 1
            if count > 1:
                return False
    return True