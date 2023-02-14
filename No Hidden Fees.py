def has_hidden_fee(prices, t):
    no_strip = []
    for x in prices:
        no_strip.append(int(x.strip("$")))
    totals = sum(no_strip)
    if totals < int(t.strip("$")):
        return True
    return False
    
    
    
    