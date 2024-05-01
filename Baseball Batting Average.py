def batting_avg(season):
    total_hits = 0
    total_at_bats = 0
    for game in season:
        hits, at_bats = game
        total_hits += hits
        total_at_bats += at_bats
    if total_at_bats == 0:
        return ".000"
    else:
        avg = total_hits / total_at_bats
        return "{:.3f}".format(avg)[1:]
