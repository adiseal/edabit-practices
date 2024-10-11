def is_prob_matrix(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return False
    
    # Check each row
    for row in matrix:
        # Check if all elements are between 0 and 1
        if not all(0 <= x <= 1 for x in row):
            return False
        # Check if the row sums to 1
        if not round(sum(row), 10) == 1:  # Using rounding to handle floating-point precision
            return False
    
    return True
