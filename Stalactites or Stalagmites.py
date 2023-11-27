def mineral_formation(cave):
    top = any(cave[0])
    bottom = any(cave[-1])
    if top and bottom:
        return "both"
    elif top:
        return "stalactites"
    else:
        return "stalagmites"
