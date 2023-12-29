def get_total_price(groceries):
    total = 0
    for grocery in groceries:
        total += grocery["quantity"] * grocery["price"]
    return round(total, 2)
