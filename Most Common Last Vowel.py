import re
from collections import Counter

def common_last_vowel(sentence):
    # Define vowels
    vowels = "aeiou"
    
    # Find all words in the sentence
    words = re.findall(r'\b\w+\b', sentence.lower())
    
    # Extract the last vowel from each word
    last_vowels = []
    for word in words:
        for char in reversed(word):
            if char in vowels:
                last_vowels.append(char)
                break
    
    # Count the frequency of each last vowel
    vowel_counts = Counter(last_vowels)
    
    # Find the most common last vowel
    most_common_vowel = vowel_counts.most_common(1)[0][0]
    
    return most_common_vowel