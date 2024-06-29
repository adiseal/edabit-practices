import re

def average_word_length(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)
    
    words = sentence.split()
    
    total_length = sum(len(word) for word in words)
    
    average_length = total_length / len(words)
    
    average_length = round(average_length, 2)
    
    return average_length