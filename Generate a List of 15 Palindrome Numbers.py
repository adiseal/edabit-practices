def generate_palindromes(limit):
    # Create a list of palindromes from 10 to the given limit
    palindromes = [n for n in range(10, limit + 1) if str(n) == str(n)[::-1]]
    
    # Return the last 15 palindromes sorted in ascending order
    return palindromes[-15:]