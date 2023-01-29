import re

def reverse_title(txt):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].lower() + mo.group(0)[1:].upper(), txt)
    
    
    
assert reverse_title("this is a title") == "tHIS iS a tITLE"

assert reverse_title("BOLD AND BRASH!") == "bOLD aND bRASH!"

assert reverse_title("Elephants dance about bravely in Thailand") == "eLEPHANTS dANCE aBOUT bRAVELY iN tHAILAND"