def time_to_finish(full: str, unfinished: str) -> float:
    # Calculate the number of characters left to write
    num_chars = len(full) - len(unfinished)
    
    # Remove the count of spaces from num_chars
    num_chars -= full.count(' ', len(unfinished))
    
    # Multiply by 0.5 to get the time in seconds
    time = num_chars * 0.5
    
    return time