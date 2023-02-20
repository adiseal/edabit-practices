def hurdle_jump(hurdles, jump_height):
    max_val = max(hurdles) if hurdles else 0
	return True if max_val <= jump_height else False