def has_syncopation(beats):
    return any(beats[i] == '#' for i in range(1, len(beats), 2))