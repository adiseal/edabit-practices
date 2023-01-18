def roger_shots(lst):
	return (lst.count("Bang!") / 2) + (lst.count("BangBang!") / 2)


assert roger_shots(["Bang!", "Bang!", "Bang!", "Bang!", "Bang!", "Bang!"]) == 3

assert roger_shots(["Bang!", "Bang!", "Bang!", "Bang!", "BangBang!"]) == 2.5

assert roger_shots(["Bang!", "BangBangBang!", "Boom!", "Bang!", "BangBang!", "BangBang!"]) == 2

#print(1/2)    