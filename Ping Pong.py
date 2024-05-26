def ping_pong(pings, win):
    game_sequence = []    
    for ping in pings:
        game_sequence.extend([ping, "Pong!"])
    if not win:
        game_sequence.pop()
    return game_sequence