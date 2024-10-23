from collections import Counter

def min_removals(s1, s2):
    # Count frequency of each character in both strings
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Calculate the total removals needed
    removals = 0
    
    # Get all unique characters from both strings
    unique_chars = set(count1.keys()).union(set(count2.keys()))
    
    # Compare the frequencies and add the difference to removals
    for char in unique_chars:
        removals += abs(count1.get(char, 0) - count2.get(char, 0))
    
    return removals