def robot_path(commands):
    destination_1 = ['e', 'n', 'e', 'e', 'n']
    destination_2 = ['w', 'n', 'w', 'n', 'w', 'w', 'n']

    # Check if the commands end with either of the destinations
    if commands[-len(destination_1):] == destination_1 or commands[-len(destination_2):] == destination_2:
        return True
    else:
        return False
