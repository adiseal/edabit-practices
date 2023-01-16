def find_letters(word):
    unique_letters = []
    for i in word:
        if word.count(i) == 1:
            unique_letters.append(i)
    return unique_letters
                
        
        
        
assert find_letters("monopoly") == ["m", "n", "p", "l", "y"]

assert find_letters("balloon") == ["b", "a", "n"]

assert find_letters("analysis") == ["n", "l", "y", "i"]