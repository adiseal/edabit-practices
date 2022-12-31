def keyboard_mistakes(txt):
    txt = txt.replace("4", "A")
    txt = txt.replace("5", "S")
    txt = txt.replace("1", "I")
    txt = txt.replace("0", "O")
    return txt
    



assert keyboard_mistakes("MUB45H1R") == "MUBASHIR"

assert keyboard_mistakes("DUBL1N") == "DUBLIN"

assert keyboard_mistakes("51NG4P0RE") == "SINGAPORE"