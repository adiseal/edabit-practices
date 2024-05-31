def delete_occurrences(lst, num):
    result = []
    for element in lst:
        if result.count(element) < num:
            result.append(element)
    return result