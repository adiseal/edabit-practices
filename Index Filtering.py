def index_filter(indexes, string):
    return ''.join(string[i].lower() for i in indexes)

print(index_filter([2, 3, 8, 11], "Autumn in New York")) # "tune"