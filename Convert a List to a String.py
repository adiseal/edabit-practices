def list_to_string(lst):
    full_str = "".join(str(elem) for elem in lst)
    return full_str
    

assert list_to_string([1, 2, 3, 4, 5, 6]) == "123456"

assert list_to_string(["a", "b", "c", "d", "e", "f"]) == "abcdef"

assert list_to_string([1, 2, 3, "a", "s", "dAAAA"]) == "123asdAAAA"