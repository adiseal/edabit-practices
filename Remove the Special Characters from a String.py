import re

def remove_special_characters(s):
    # The regex pattern to find all characters that are not a-z, A-Z, 0-9, -, _, or space
    pattern = r'[^a-zA-Z0-9-_ ]'
    # Use the sub() method to replace them with an empty string
    return re.sub(pattern, "", s)

print(remove_special_characters("The quick brown fox!")) # "The quick brown fox"
print(remove_special_characters("%fd76$fd(-)6GvKlO.")) # "fd76fd-6GvKlO"
print(remove_special_characters("D0n$c sed 0di0 du1")) # "D0nc sed 0di0 du1"