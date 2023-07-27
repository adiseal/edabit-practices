def greet_people(names):
    greetings = ["Hello " + name for name in names]
    return ", ".join(greetings)
