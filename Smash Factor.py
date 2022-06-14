# Author    : Adi Nugroho
# Date      : Jun/14/2022
# a function that takes ball speed bs and club speed cs as arguments 
# and returns the smash factor to the nearest hundredth

def smash_factor(bs, cs):
    return round(bs / cs, 2)
	
# print(smash_factor(181.2, 124.5)) # ➞ 1.46