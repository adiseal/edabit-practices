def area_of_country(name, area):
	return name + " is " + str(round(((area/148940000)*100),2)) +"% of the total world's landmass"

print(area_of_country("Iran", 1648195)) # "Iran is 1.11% of the total world's landmass"