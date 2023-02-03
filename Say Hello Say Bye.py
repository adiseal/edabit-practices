def say_hello_bye(name, num):
    if num == 1:
        return "Hello " + name.title()
    else:
        return "Bye " + name.title()
    
assert say_hello_bye("alon", 1) == "Hello Alon"

assert say_hello_bye("Tomi", 0) == "Bye Tomi"

assert say_hello_bye("jose", 0) == "Bye Jose"