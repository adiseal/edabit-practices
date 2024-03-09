def is_mini_sudoku(square):
    numbers = set()
    for row in square:
        for num in row:
            if num < 1 or num > 9 or num in numbers:
                return False
            numbers.add(num)
    return True