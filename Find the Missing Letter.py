def missing_letter(letters):
    for i in range(len(letters) - 1):
        if ord(letters[i + 1]) != ord(letters[i]) + 1:
            return chr(ord(letters[i]) + 1)