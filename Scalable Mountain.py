def is_scalable(mountain):
    for i in range(1, len(mountain)):
        if abs(mountain[i] - mountain[i-1]) > 5:
            return False
    return True