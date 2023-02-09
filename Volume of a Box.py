def volume_of_box(sizes):
    result = 1
    for x in sizes:
        result = result * sizes[x]
    return result

print(volume_of_box({ "width": 2, "length": 5, "height": 1 })) #➞ 10