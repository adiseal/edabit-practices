def format_ascii(ascii_string, width):
    groups = [ascii_string[i:i+width] for i in range(0, len(ascii_string), width)]    
    return '\n'.join(groups)