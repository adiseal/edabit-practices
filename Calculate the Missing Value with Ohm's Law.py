def ohms_law(v, r, i):
    if (v is None and r is not None and i is not None):
        return round(r * i, 2)
    elif (r is None and v is not None and i is not None):
        return round(v / i, 2)
    elif (i is None and v is not None and r is not None):
        return round(v / r, 2)
    else:
        return "Invalid"
