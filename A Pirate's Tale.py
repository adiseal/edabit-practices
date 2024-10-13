def number_of_days(destination):
    x, y = destination
    # Calculate total distance
    total_distance = abs(x) + abs(y)
    
    # Calculate travel days
    travel_days = total_distance
    
    # Calculate rest days
    rest_days = (travel_days - 1) // 5
    
    # Total days
    total_days = travel_days + rest_days
    
    return total_days