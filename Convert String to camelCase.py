def to_camel_case(text):
    if not text:
        return ""
    
    # Split the string by dashes or underscores
    words = text.replace("-", "_").split("_")
    
    # Keep the first word as is, the rest are capitalized
    return words[0] + ''.join(word.capitalize() for word in words[1:])