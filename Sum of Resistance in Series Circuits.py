def series_resistance(lst):
    total_resistance = sum(lst)
    if total_resistance <= 1:
        return str(total_resistance) + ' ohm'
    else:
        return str(total_resistance) + ' ohms'

print(series_resistance([1, 5, 6, 3])) # "15 ohms"