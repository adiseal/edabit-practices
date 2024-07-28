def same_upsidedown(s):
    # Create a mapping for the digits when turned upside down
    upside_down_mapping = {'0': '0', '6': '9', '9': '6'}
    
    # Generate the upside down version of the string
    upside_down = []
    
    for char in reversed(s):
        if char in upside_down_mapping:
            upside_down.append(upside_down_mapping[char])
        else:
            return False  # If there are any invalid characters
    
    # Join the list to form the final upside down string
    upside_down_str = ''.join(upside_down)
    
    # Check if the original string is the same as the upside down version
    return upside_down_str == s