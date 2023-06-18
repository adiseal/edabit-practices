def mean(numbers):
    if not numbers:
        return 0  # Handle the case of an empty array
    
    total = sum(numbers)
    mean_value = total / len(numbers)
    return round(mean_value, 2)
	
print(mean([1, 0, 4, 5, 2, 4, 1, 2, 3, 3, 3])) # 2.55