def forbidden_letter(char, lst):
    char_in_list = not any(char in i for i in lst)
    return char_in_list
    

assert forbidden_letter("r", ["rock", "paper", "scissors"]) == False

assert forbidden_letter("a", ["spoon", "fork", "knife"]) == True

assert forbidden_letter("m", []) == True