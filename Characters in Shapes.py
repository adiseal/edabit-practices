def count_characters(shape):
    count = 0
    for row in shape:
        count += len(row)
    return count
