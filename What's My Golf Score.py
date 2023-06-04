def golf_score(course,result):
    score = 0
    index = 0
    while index < len(course):
        if result[index] == "eagle":
            score += course[index] - 2
        elif result[index] == "birdie":
            score += course[index] - 1
        elif result[index] == "bogey":
            score += course[index] + 1
        elif result[index] == "double-bogey":
            score += course[index] + 2
        elif result[index] == "par":
            score += course[index]
        index += 1
    return score
    