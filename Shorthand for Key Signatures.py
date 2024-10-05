import re

def full_key_name(music_piece):
    # Define a regex to capture the key signature after "in"
    pattern = r"in\s([a-gA-G][b#]?)"
    
    def replace_key(match):
        key = match.group(1)
        # Use traditional string formatting for minor/major
        if key.islower():
            full_key = "{} minor".format(key.capitalize())
        else:
            full_key = "{} major".format(key)
        return "in {}".format(full_key)
    
    # Substitute the pattern in the string
    return re.sub(pattern, replace_key, music_piece)
