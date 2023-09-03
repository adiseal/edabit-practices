def remove_dups(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst

print(remove_dups([1, 0, 1, 0])) # [1, 0]
print(remove_dups(["The", "big", "cat"])) # ["The", "big", "cat"]
print(remove_dups(["John", "Taylor", "John"])) # ["John", "Taylor"]