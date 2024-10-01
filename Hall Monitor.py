def possible_path(path):
    # Initialize a variable to keep track of whether the last element was a room or hallway
    last_was_hallway = True  # Start with True to allow starting with 'H'
    
    for item in path:
        if isinstance(item, int):  # If the item is a room
            if not last_was_hallway:  # If the last was not a hallway, return False
                return False
            last_was_hallway = False  # Now we are in a room
        elif item == "H":  # If the item is a hallway
            last_was_hallway = True  # We can move back to hallway
    
    return True  # If we finish checking without issues, return True