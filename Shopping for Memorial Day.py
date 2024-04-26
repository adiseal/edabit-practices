tax = .06
def checkout(items):
    total = 0
    for item in items:
        subtotal = item["prc"] * item["qty"]
        if item["taxable"]:
            subtotal *= 1.06  
        total += subtotal
    return round(total, 2)  
	