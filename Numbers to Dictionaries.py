def num_to_dict(lst):
    char = [chr(num) for num in lst]
    mydict = []
    for x in range(0, len(lst)):
        mydict.append(dict(zip([str(lst[x])], char[x])))
    return mydict
    
    
    

print(num_to_dict([101, 121, 110, 113, 103])) #➞ [{"101":"e"}, {"121":"y"}, {"110":"n"}, {"113":"q"}, {"103":"g"}]
