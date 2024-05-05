def keys_and_values(d):
    sorted_keys = sorted(d.keys())
    sorted_values = [d[key] for key in sorted_keys]
    return [sorted_keys, sorted_values]