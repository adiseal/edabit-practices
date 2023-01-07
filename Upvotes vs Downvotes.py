def get_vote_count(votes):
	return votes.get("upvotes") - votes.get("downvotes") 


assert get_vote_count({ "upvotes": 13, "downvotes": 0 }) == 13

assert get_vote_count({ "upvotes": 2, "downvotes": 33 }) == -31

assert get_vote_count({ "upvotes": 132, "downvotes": 132 }) == 0