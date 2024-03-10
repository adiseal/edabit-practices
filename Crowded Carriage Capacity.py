def find_a_seat(n, carriages):
    max_capacity_per_carriage = n / len(carriages)
    for i, carriage in enumerate(carriages):
        if carriage <= 0.5 * max_capacity_per_carriage:
            return i
    return -1
