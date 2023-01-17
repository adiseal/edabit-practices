def same_case(txt):
    return txt.islower() or txt.isupper()


assert same_case("hello") == True

assert same_case("HELLO") == True

assert same_case("Hello") == False

assert same_case("ketcHUp") == False