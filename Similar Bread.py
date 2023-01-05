def has_same_bread(lst1, lst2):
    return lst1[::len(lst1)-1] == lst2[::len(lst2)-1]



assert has_same_bread(["white bread", "lettuce", "white bread"],["white bread", "tomato", "white bread"]) == True

assert has_same_bread(["brown bread", "chicken", "brown bread"],["white bread", "chicken", "white bread"]) == False

assert has_same_bread(["toast", "cheese", "toast"],["brown bread", "cheese", "toast"]) == False