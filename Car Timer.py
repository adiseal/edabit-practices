def car_timer(n):
    hours, minutes = divmod(n, 60)
    time_str = str(hours).zfill(2) + str(minutes).zfill(2)
    digit_sum = sum(int(digit) for digit in time_str)
    return digit_sum