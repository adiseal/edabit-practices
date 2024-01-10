def lottery(ticket, win):
    mini_wins = 0
    for sublist in ticket:
        string, number = sublist
        for char in string:
            if ord(char) == number:
                mini_wins += 1
                break
    if mini_wins >= win:
        return "Winner!"
    else:
        return "Loser!"
