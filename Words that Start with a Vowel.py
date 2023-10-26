import re

def retrieve(sentence):
    # Use regular expression to find words that start with a vowel
    words = re.findall(r'\b[aeiouAEIOU][a-zA-Z]*\b', sentence.lower())
    
    # Convert words to lowercase
    words = [word.lower() for word in words]
    
    return words
    
print(retrieve("A simple life is a happy life for me.")) # ["a", "is", "a"]
print(retrieve("Exercising is a healthy way to burn off energy.")) # ["exercising", "is", "a", "off", "energy"]
print(retrieve("The poor ostrich was ostracized.")) # ["ostrich", "ostracized"]
print(retrieve("")) # []