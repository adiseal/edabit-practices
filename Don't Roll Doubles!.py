def dice_game(rolls):
    score = 0
    for roll in rolls:
        if roll[0] == roll[1]:  
            return 0
        score += sum(roll)  
    return score