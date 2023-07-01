def mood_today(mood=None):
    if mood:
        return "Today, I am feeling " + mood
    else:
        return "Today, I am feeling neutral"

print(mood_today("happy")) # "Today, I am feeling happy"