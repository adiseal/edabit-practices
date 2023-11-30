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

print(spin_around(['left', 'right', 'left', 'right'])) # 0
print(spin_around(['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'])) # 2
print(spin_around(['left', 'left', 'left', 'left'])) # 1
print(spin_around([])) # 0
print(spin_around(['left'])) # 0
print(spin_around(['right'])) # 0
print(spin_around(['right', 'right', 'right', 'left', 'right', 'right'])) # 1
print(spin_around(['left', 'left', 'right', 'left', 'left', 'left', 'left', 'left', 'left', 'right', 'left', 'left', 'right', 'right', 'right', 'right', 'left', 'left', 'right', 'right'])) # 1