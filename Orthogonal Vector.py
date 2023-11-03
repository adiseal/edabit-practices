def is_orthogonal(first, second):
    # Calculate the dot product
    dot_product = sum(i*j for i, j in zip(first, second))
    # Check if the dot product is zero
    return dot_product == 0

print(is_orthogonal([1, 2], [2, -1])) # True
print(is_orthogonal([3, -1], [7, 5])) # False
print(is_orthogonal([1, 2, 0], [2, -1, 10])) # True