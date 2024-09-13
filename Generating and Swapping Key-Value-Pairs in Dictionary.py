def swap_d(keys, values, swap):
    if len(keys) != len(values):
        raise ValueError("Lists must be of the same length")

    if swap:
        return dict(zip(values, keys))
    else:
        return dict(zip(keys, values))