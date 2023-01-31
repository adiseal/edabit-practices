def rev(n):
    string_n = str(n)
    string_n = string_n.replace("-", "")
    return string_n[::-1]


assert rev(5121) == "1215"

assert rev(69) == "96"

assert rev(-122157) == "751221"
    