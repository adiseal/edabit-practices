def prevent_distractions(string):
    distractions = ["anime", "meme", "vines", "roasts", "Danny DeVito"]
    for distraction in distractions:
        if distraction.lower() in string.lower():
            return "NO!"
    return "Safe watching!"

print(prevent_distractions("vines that butter my eggroll")) # "NO!"