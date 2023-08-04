def remove_vowels(string):
    vowels = "aeiouAEIOU"
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string
    
print(remove_vowels("I have never seen a thin person drinking Diet Coke.")) # " hv nvr sn  thn prsn drnkng Dt Ck."
print(remove_vowels("We're gonna build a wall!")) # "W'r gnn bld  wll!"
print(remove_vowels("Happy Thanksgiving to all--even the haters and losers!")) # "Hppy Thnksgvng t ll--vn th htrs nd lsrs!"