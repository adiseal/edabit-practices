                
def find_single_number(numbers):
    if numbers == []:
        return None
    for i in numbers:
        if numbers.count(i) <= 1:
            return i
            


assert find_single_number([2, 2, 2, 3, 4, 4, 4]) == 3

assert find_single_number([2]) == 2

assert find_single_number([]) == None

assert find_single_number([7, 13, 3, 6, 5, 4, 4, 13, 5, 3, 6, 7, 6, 5, 3, 13, 4, 7, 13, 5, 7, 4, 3, 6, 8, 4, 3, 7, 5, 6, 13]) == 8

assert find_single_number([1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 101, 4, 3, 1, 5, 6, 2]) == 101