def after_n_years(names, n):
    result = {}
    for person, age in names.items():
        new_age = age + abs(n)
        result[person] = new_age
    return result