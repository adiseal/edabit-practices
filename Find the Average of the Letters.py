import string

def average_index(letters):
    lst_index = []
    print(lst_index)
    lst = list(string.ascii_lowercase)
    for x in letters:
        index = lst.index(x) + 1
        lst_index.append(index)
    print(lst_index)
    return round(sum(lst_index) / len(lst_index), 2)
        
        
print(average_index(['a','b','c','i'])) #➞ 3.75
print(average_index(['e','d','a','b','i','t'])) # 6.83
print(average_index(['o','m','g']))