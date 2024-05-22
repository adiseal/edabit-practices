def empty_values(lst):
    result = []
    for value in lst:
        if isinstance(value, int):
            result.append(0)
        elif isinstance(value, float):
            result.append(0.0)
        elif isinstance(value, str):
            result.append("")
        elif isinstance(value, bool):
            result.append(False)
        elif isinstance(value, list):
            result.append([])
        elif isinstance(value, tuple):
            result.append(())
        elif isinstance(value, set):
            result.append(set())
        else:
            result.append(value)  # Preserve None and other types
    return result