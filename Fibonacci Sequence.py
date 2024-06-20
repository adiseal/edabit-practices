def fibonacci_sequence():
    sequence = [0, 1]
    while True:
        next_value = sequence[-1] + sequence[-2]
        if next_value >= 255:
            break
        sequence.append(next_value)
    return sequence