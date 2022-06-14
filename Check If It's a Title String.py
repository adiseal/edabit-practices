# Author    : Adi Nugroho
# Date      : Jun/14/2022
# Check if a string txt is a title text or not 
# A title text is one which has all the words in the text start with an upper case letter

def check_title(txt):
    return txt.istitle()

# print(check_title("Water Is Transparent")) -> True
# print(check_title("Water is Transparent")) -> False