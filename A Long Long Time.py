def longest_time(h, m, s):
    h = h * 60 * 60
    m = m * 60
    if h > m and h > s:
        return h // 3600
    elif m > h and m > s:
        return m // 60
    else:
        return s
