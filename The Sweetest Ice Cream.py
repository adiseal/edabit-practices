class IceCream:
    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles

# Dictionary for sweetness values of each flavor
sweetness_values = {
    "Plain": 0,
    "Vanilla": 5,
    "ChocolateChip": 5,
    "Strawberry": 10,
    "Chocolate": 10
}

def sweetest_icecream(icecreams):
    # Calculate sweetness for each ice cream
    def calculate_sweetness(icecream):
        # Sweetness is the base flavor sweetness plus the number of sprinkles
        return sweetness_values[icecream.flavor] + icecream.num_sprinkles
    
    # Find the max sweetness value
    return max(calculate_sweetness(icecream) for icecream in icecreams)