def chess_board(coordinate):
    letter, number = coordinate[0], int(coordinate[1])
    letter_value = ord(letter) - ord('a') + 1
    total = letter_value + number
    return "black" if total % 2 == 0 else "white"