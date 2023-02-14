def free_shipping(order):
    totals = sum(order.values())
    if totals > 50.00:
        return True
    return False
    
    
assert free_shipping({ "Shampoo": 5.99, "Rubber Ducks": 15.99 }) == False

assert free_shipping({ "Flatscreen TV": 399.99 }) == True

assert free_shipping({ "Monopoly": 11.99, "Secret Hitler": 35.99, "Bananagrams": 13.99 }) == True