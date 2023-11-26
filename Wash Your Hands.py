def wash_hands(N, nM):
    total_seconds = N * 21 * nM * 30
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return "{} minutes and {} seconds".format(minutes, seconds)