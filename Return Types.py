def list_values_types(lst):
    types = []
    for x in lst:
        types.append(type(x).__name__)
    return types
    
    
assert list_values_types(["shashwat", 10, 90]) == ["str", "int", "int"]