def bomb(txt):
    if "bomb" in txt.casefold():
        return "Duck!!!"
    return "There is no bomb, relax."


assert bomb("There is a bomb.") == "Duck!!!"

assert bomb("Hey, did you think there is a bomb?") == "Duck!!!"

assert bomb("This goes boom!!!") == "There is no bomb, relax."