def fruit_salad(fruits):
    chunks = []
    for fruit in fruits:
        mid = len(fruit) // 2
        if len(fruit) % 2 == 0:  # If the fruit has an even number of letters
            chunks.append(fruit[:mid])
            chunks.append(fruit[mid:])
        else:  # If the fruit has an odd number of letters
            chunks.append(fruit[:mid])
            chunks.append(fruit[mid:])
    chunks.sort()
    return "".join(chunks)