def correct_signs(txt):
    parts = txt.split()
    for i in range(0, len(parts)-2, 2):
        if not eval(parts[i] + parts[i+1] + parts[i+2]):
            return False
    return True
