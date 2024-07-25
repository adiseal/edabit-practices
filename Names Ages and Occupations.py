def organize(info_string):
    # Check if the input string is empty
    if not info_string:
        return {}
    
    # Split the input string by commas and strip whitespace
    parts = [part.strip() for part in info_string.split(',')]
    
    # Ensure we have exactly three parts
    if len(parts) != 3:
        raise ValueError("Input must contain exactly three parts: name, age, and occupation.")
    
    # Map the parts to the corresponding keys
    return {
        "name": parts[0],
        "age": int(parts[1]),  # Convert age to an integer
        "occupation": parts[2]
    }