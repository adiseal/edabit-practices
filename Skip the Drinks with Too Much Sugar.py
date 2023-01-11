def skip_the_sugar(drinks):
    filtered = []
    for drink in drinks:
        if drink != "fanta" and drink != "cola":
            filtered.append(drink)
    return filtered
    

assert skip_the_sugar(["fanta", "cola", "water"]) == ["water"]

assert skip_the_sugar(["fanta", "cola"]) == []

assert skip_the_sugar(["lemonade", "beer", "water"]) == ["lemonade", "beer", "water"]