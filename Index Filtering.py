def index_filter(indexes, string):
    return ''.join(string[i].lower() for i in indexes)

print(index_filter([2, 3, 8, 11], "Autumn in New York")) # "tune"
print(index_filter([0, 1, 5, 7, 4, 2], "Cry me a river")) # "creamy"
print()index_filter([9, -9, 2, 27, 36, 6, 5, 13, -1, 2, 0, 30, 2], "That's life, I've got you under my skin") # "frank sinatra"