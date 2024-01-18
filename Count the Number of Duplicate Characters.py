def duplicates(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return sum(count - 1 for count in counts.values() if count > 1)
