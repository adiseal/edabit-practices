def trimmed_averages(lst):
    lst.remove(max(lst))
    lst.remove(min(lst))
    average = round(sum(lst) / len(lst))
    return average


assert trimmed_averages([4, 5, 7, 100]) == 6
# Average of 5 and 7

assert trimmed_averages([10, 25, 5, 15, 20]) == 15
# Average of 10, 15 and 20

assert trimmed_averages([1, 1, 1]) == 1
# 1

        