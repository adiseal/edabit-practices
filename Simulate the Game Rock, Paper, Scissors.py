import numpy as np

def rps(player1, player2):
    # Define the possible moves
    moves = ["rock", "paper", "scissors"]
    
    # Create a lookup table using NumPy
    # 0 = tie, 1 = player 1 wins, 2 = player 2 wins
    lookup_table = np.array([
        [0, 2, 1],
        [1, 0, 2],
        [2, 1, 0]
    ])
    
    # Get the indices of the players' moves
    p1_index = moves.index(player1)
    p2_index = moves.index(player2)
    
    # Look up the result in the table
    result = lookup_table[p1_index, p2_index]
    
    # Return the appropriate string based on the result
    if result == 0:
        return "TIE"
    elif result == 1:
        return "Player 1 wins"
    else:
        return "Player 2 wins"