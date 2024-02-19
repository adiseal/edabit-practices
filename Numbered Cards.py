def win_round(you, opponent):
    you.sort(reverse=True)
    opponent.sort(reverse=True)
    your_number = int(str(you[0]) + str(you[1]))
    opponent_number = int(str(opponent[0]) + str(opponent[1]))
    return your_number > opponent_number