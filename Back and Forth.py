def calculate_arrowhead(lst):
    right_moves = 0
    left_moves = 0
    
    # Count the number of right and left moves
    for arrows in lst:
        right_moves += arrows.count(">")
        left_moves += arrows.count("<")
    
    # Calculate net movement
    net_movement = right_moves - left_moves
    
    # Determine the direction of the net movement
    if net_movement > 0:
        return ">" * net_movement
    elif net_movement < 0:
        return "<" * abs(net_movement)
    else:
        return ""