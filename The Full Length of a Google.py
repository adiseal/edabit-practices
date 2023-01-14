def googlify(n):
    if n <= 1:
        return "invalid"
    return "G" + "o" * n + "gle"



assert googlify(10) == "Goooooooooogle"

assert googlify(23) == "Gooooooooooooooooooooooogle"

assert googlify(0) == "invalid"

assert googlify(-5) == "invalid"