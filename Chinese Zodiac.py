def chinese_zodiac(year):
    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"]
    start_year = 1900  # The first year in the Chinese zodiac cycle
    offset = (year - start_year) % 12
    return animals[offset]
    
print(chinese_zodiac(2021)) # "Ox"