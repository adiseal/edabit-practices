def color_pattern_times(cols):
    color_time = 2 * len(cols)
    
    switch_time = 0
    
    for i in range(1, len(cols)):
        if cols[i] != cols[i - 1]:
            switch_time += 1
    
    return color_time + switch_time