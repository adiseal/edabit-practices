def find_broken_keys(correct, typed):
    broken = []
    for c, t in zip(correct, typed):
        if c != t and c not in broken:
            broken.append(c)
    return broken