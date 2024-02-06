def diving_minigame(altitudes):
    breath_meter = 10
    for altitude in altitudes:
        if altitude < 0:  
            breath_meter -= 2
        else:  
            breath_meter = min(10, breath_meter + 4)
        if breath_meter <= 0:  
            return False
    return True