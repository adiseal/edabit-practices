def single_occurrence(txt):
    if txt == "":
        return ""
    ups = txt.upper()
    for x in ups:
        if ups.count(x) == 1:
            return x        
