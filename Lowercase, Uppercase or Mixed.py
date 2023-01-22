def get_case(txt):
    if txt[1:] == txt[1:].upper():
        return "upper"
    elif txt[1:] == txt[1:].lower():
        return "lower"
    else:
        return "mixed"


assert get_case("whisper...") == "lower"

assert get_case("SHOUT!") == "upper"

assert get_case("Indoor Voice") == "mixed"	