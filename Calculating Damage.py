def damage(damage, speed, time):
	if damage < 0 or speed < 0:
		return "invalid"
	elif time == "second":
		return damage * speed
	elif time == "minute":
		return damage * speed * 60
	elif time == "hour":
		return damage * speed * 60 * 60
        
print(damage(2, 100, "hour")) # 720000