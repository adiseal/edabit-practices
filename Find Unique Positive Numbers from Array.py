def unique_lst(lst):
    seen = set()
    result = []
    for num in lst:
        if num > 0 and num not in seen:
            seen.add(num)
            result.append(num)
    return result
