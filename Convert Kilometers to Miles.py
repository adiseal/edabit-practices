def km_to_miles(kilometers):
	km = kilometers * 0.6213711
	return round(km, 5)


assert km_to_miles(2) == 1.24274

assert km_to_miles(6) == 3.72823

assert km_to_miles(8) == 4.97097