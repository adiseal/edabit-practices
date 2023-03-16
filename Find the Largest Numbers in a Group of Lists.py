def findLargestNums(lst):
	a = []
	for i in lst:
		a = a + [max(i)]
	return a
	
print(findLargestNums([[-34, -54, -74], [-32, -2, -65], [-54, 7, -43]])) # [-34, -2, 7]