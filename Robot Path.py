def robot_path(commands):
    destination_1 = ["e", "n", "e", "e", "n"]
    destination_2 = ["w", "n", "w", "n", "w", "w", "n"]

    # Filter out the commands that are not in the destinations
    filtered_commands = [command for command in commands if command in destination_1 or command in destination_2]

    # Check if the filtered commands end with either destination
    return filtered_commands[-len(destination_1):] == destination_1 or filtered_commands[-len(destination_2):] == destination_2