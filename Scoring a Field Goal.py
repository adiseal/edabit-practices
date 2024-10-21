def is_goal_scored(goal):
    # Iterate through each row until the crossbar
    for row in goal[:3]:
        # Check if the ball '0' is between the goalposts '#'
        if '0' in row[0][2:9]:
            return True
    return False