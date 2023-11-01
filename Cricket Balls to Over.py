def total_overs(balls):
    overs = balls // 6
    remaining_balls = balls % 6
    return float("%s.%s" % (overs, remaining_balls))