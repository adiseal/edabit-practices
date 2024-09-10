def fire(matrix, coord):
    # Create a mapping for rows A-E to matrix indices
    row_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    
    # Get the row and column from the coordinate
    row = row_mapping[coord[0]]  # Letter part
    col = int(coord[1]) - 1      # Number part
    
    # Check the matrix at the given position
    if matrix[row][col] == '*':
        return "BOOM"
    else:
        return "splash"