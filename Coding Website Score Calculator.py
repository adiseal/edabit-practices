def score_calculator(easy, med, hard):
	return (easy * 5) + (med * 10) + (hard * 20) if easy >= 0 and med >= 0 and hard >= 0 else "invalid"


assert score_calculator(1, 2, 3) == 85

assert score_calculator(1, 0, 10) == 205

assert score_calculator(5, 2, -6) == "invalid"    