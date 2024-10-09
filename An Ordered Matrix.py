def ordered_matrix(a, b):
    # Initialize an empty matrix
    matrix = []
    
    # Fill the matrix with ordered values
    for i in range(a):
        row = []  # Create a new row
        for j in range(b):
            # Calculate the value based on row and column indices
            value = i * b + j + 1
            row.append(value)  # Add the value to the current row
        matrix.append(row)  # Add the completed row to the matrix
    
    return matrix