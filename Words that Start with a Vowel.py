import re

def retrieve(sentence):
    # Use regular expression to find words that start with a vowel
    words = re.findall(r'\b[aeiouAEIOU][a-zA-Z]*\b', sentence.lower())
    
    # Convert words to lowercase
    words = [word.lower() for word in words]
    
    return words