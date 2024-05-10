def describe_num(n):
    words = {
        1: "brilliant",
        2: "exciting",
        3: "fantastic",
        4: "virtuous",
        5: "heart-warming",
        6: "tear-jerking",
        7: "beautiful",
        8: "exhilarating",
        9: "emotional",
        10: "inspiring"
    }
    description = "The most"
    for i in range(1, 11):
        if n % i == 0:
            description += " " + words[i]
    description += " number is " + str(n) + "!"
    return description