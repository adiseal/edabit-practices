def football_points(wins, draws, losses): # (3,3,2)
	index = 1 # 1
	score = [wins,draws,losses]
	while index <= len(score): # 3
		if index == 1:
			wins = score[0] # 3 
			sum_wins = 3 * wins # 9
			#print(sum_wins)
			index += 1
		elif index == 2:
			draws = score[1] #3
			sum_draws = 1 * draws # 3
			#print(sum_draws)
			index += 1
		else:
		    losses = score[2] #2
		    sum_losses = 0 * losses # 0
		    #print(sum_losses)
		    index += 1
	result = sum_wins + sum_draws + sum_losses
	return result
    
print(football_points(3, 4, 2)) # 13
print(football_points(5, 0, 2)) # 15
print(football_points(0, 0, 1)) # 0