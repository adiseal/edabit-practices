def simple_timer(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    return timer

print(simple_timer(0)) # "00:00:00"