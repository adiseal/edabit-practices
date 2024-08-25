def camelCasing(s: str) -> str:
    # Remove underscores and split the string by spaces
    words = s.replace('_', ' ').split()
    
    # Convert the first word to lowercase, and capitalize subsequent words
    camel_case_str = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    
    return camel_case_str