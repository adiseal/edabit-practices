def reverse_title(txt):
    title = txt.title()
    return title.swapcase()
    
assert reverse_title("this is a title") == "tHIS iS a tITLE"

assert reverse_title("BOLD AND BRASH!") == "bOLD aND bRASH!"

assert reverse_title("Elephants dance about bravely in Thailand") == "eLEPHANTS dANCE aBOUT bRAVELY iN tHAILAND"
