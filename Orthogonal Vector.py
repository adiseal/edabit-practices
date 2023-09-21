def is_orthogonal(first, second):
    # Calculate the dot product
    dot_product = sum(i*j for i, j in zip(first, second))
    # Check if the dot product is zero
    return dot_product == 0
