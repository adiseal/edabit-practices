def get_only_evens(numbers):
    return [num for i, num in enumerate(numbers) if i % 2 == 0 and num % 2 == 0]

print(get_only_evens([1, 3, 2, 6, 4, 8])) # [2, 4]
print(get_only_evens([0, 1, 2, 3, 4])) # [0, 2, 4]