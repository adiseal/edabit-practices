# Examples: get_container("Bread") ➞ "bag"

def get_container(product):
    if product == "Bread":
        return "bag"
    elif product == "Beer" or product == "Milk":
        return "bottle"
    elif product == "Candy":
        return "plastic"
    elif product == "Eggs":
        return "carton"
    elif product == "Cheese":
        return None