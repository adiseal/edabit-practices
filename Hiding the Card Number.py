def card_hide(card):
    l= len(card) - 4
    a = ""
    for i in range(-1, -5, -1):
        a = card[i] + a
    return ("*" * l) + a

print(card_hide("8754456321113213")) # "************3213"