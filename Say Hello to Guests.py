def greet_people(names):
    greetings = ["Hello " + name for name in names]
    return ", ".join(greetings)

print(greet_people(["Joe"])) # "Hello Joe"
print(greet_people(["Angela", "Joe"])) # "Hello Angela, Hello Joe"