def spin_around(directions):
    total_rotation = 0
    
    for direction in directions:
        if direction == "right":
            total_rotation += 90
        elif direction == "left":
            total_rotation -= 90
    
    # Calculate the number of full rotations
    full_rotations = abs(total_rotation) // 360
    
    return full_rotations

