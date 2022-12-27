def determine_lever(l):
    if l == ["e", "f", "l"]:
        return "first class lever"
    elif l == ["e", "l", "f"]:
        return "second class lever"
    else:
        return "third class lever"
    
    
assert determine_lever(["e", "f", "l"]) == "first class lever"

assert determine_lever(["e", "l", "f"]) == "second class lever"

assert determine_lever(["f", "e", "l"]) == "third class lever"