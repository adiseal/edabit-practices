def is_in_range(n, r):
    if n >= r["min"] and n <= r["max"]:
        return True
    else:
        return False
        
print(is_in_range(1.8, { "min": 1.25, "max": 1.75 })) 