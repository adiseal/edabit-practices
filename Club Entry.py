def club_entry(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return (ord(word[i]) - ord('a') + 1) * 4