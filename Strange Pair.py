def is_strange_pair(str1, str2):
    if str1 == "" and str2 == "":
        return True
    elif str1 == "" or str2 == "":
        return False
    else:
        return str1[0] == str2[-1] and str1[-1] == str2[0]
