def calculate_score(games):
    # Initialize scores
    abigail_score = 0
    benson_score = 0
    
    # Define win conditions
    win_conditions = {
        ("R", "S"): "Abigail",
        ("S", "P"): "Abigail",
        ("P", "R"): "Abigail",
        ("S", "R"): "Benson",
        ("P", "S"): "Benson",
        ("R", "P"): "Benson"
    }
    
    # Calculate scores
    for game in games:
        abigail_play, benson_play = game
        if abigail_play == benson_play:
            continue  # It's a tie
        winner = win_conditions.get((abigail_play, benson_play))
        if winner == "Abigail":
            abigail_score += 1
        elif winner == "Benson":
            benson_score += 1
    
    # Determine overall winner
    if abigail_score > benson_score:
        return "Abigail"
    elif benson_score > abigail_score:
        return "Benson"
    else:
        return "Tie"
