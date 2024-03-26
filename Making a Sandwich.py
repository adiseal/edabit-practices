def make_sandwich(i, f):
    result = []
    for ingredient in i:
        if ingredient == f:
            result.extend(["bread", ingredient, "bread"])
        else:
            result.append(ingredient)
    return result