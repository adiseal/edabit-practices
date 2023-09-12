def remove_empty_arrays(arr):
    return [x for x in arr if not(isinstance(x, list) and len(x) == 0)]
