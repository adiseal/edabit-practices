def accumulating_product(lst):
    product = 1
    result = []
    for num in lst:
        product *= num
        result.append(product)
    return result