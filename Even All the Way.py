def get_only_evens(numbers):
    return [num for i, num in enumerate(numbers) if i % 2 == 0 and num % 2 == 0]
