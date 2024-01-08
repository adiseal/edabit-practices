def valid_division(d):
    try:
        numerator, denominator = map(int, d.split('/'))
        return numerator % denominator == 0
    except ZeroDivisionError:
        return "invalid"
