def calc_bundled_temp(n, temp):
    temp_value = float(temp.split('*')[0])    
    for _ in range(n):
        temp_value *= 1.1    
    return "{:.1f}*C".format(round(temp_value, 1))
