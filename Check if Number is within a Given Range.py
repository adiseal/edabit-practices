def is_in_range(n, r):
    for v in range(r["min"], r["max"]):
        if n == v:
            return True
        else:
            return False
            
print(is_in_range(4, { "min": 0, "max": 5 })) 