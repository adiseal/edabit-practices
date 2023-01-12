def modify_last(txt, n):
	return txt[0:-1] + txt[-1] * n



assert modify_last("Hello", 3) == "Hellooo"

assert modify_last("hey", 6) == "heyyyyyy"

assert modify_last("excuse me what?", 5) == "excuse me what?????"
