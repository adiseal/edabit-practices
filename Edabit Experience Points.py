def get_xp(d):
    points = {"Very Easy": 5, "Easy": 10, "Medium": 20, "Hard": 40, "Very Hard": 80}
    xp = sum([d.get(k, 0) * v for k, v in points.items()])
    return "{}XP".format(xp)
