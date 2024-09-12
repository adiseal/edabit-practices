def pages_in_book(total):
    # Check if the total is a valid sum of the first n natural numbers
    n = int((2 * total) ** 0.5)  # Estimate n using the inverse of the sum formula
    return n * (n + 1) // 2 == total