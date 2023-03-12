def is_in_range(n, r):
    for i in r:
        if i == "min":
            s = i
        else:
            i == "max"
            b = i
    if n >= r[s] and n <= r[b]:
            return True
    else:
        return False
        
print(is_in_range(5, { "min": 5, "max": 5 })) # True