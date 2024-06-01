def boom_intensity(n):
    if n < 2:
        return "boom"
    else:
        result = "B" + "o" * n + "m"
        if n % 2 == 0:
            result += "!"
        if n % 5 == 0:
            result = result.upper()
        return result