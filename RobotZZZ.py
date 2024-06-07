def robot_path(commands):
    destination1 = ["e", "n", "e", "e", "n"]
    destination2 = ["w", "n", "w", "n", "w", "w", "n"]
    
    def final_position(commands):
        x, y = 0, 0
        for command in commands:
            if command == "n":
                y += 1
            elif command == "e":
                x += 1
            elif command == "s":
                y -= 1
            elif command == "w":
                x -= 1
        return (x, y)
    
    final_pos = final_position(commands)    
    final_pos_dest1 = final_position(destination1)
    final_pos_dest2 = final_position(destination2)
    
    return final_pos == final_pos_dest1 or final_pos == final_pos_dest2