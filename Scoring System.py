def calculate_scores(txt):
    result = []
    result_count = []
    for i in txt:
        result.append(i)
    count_A = result.count("A")
    count_B = result.count("B")
    count_C = result.count("C")
    result_count = [count_A, count_B, count_C]
    return result_count


assert calculate_scores("A") == [1, 0, 0]

assert calculate_scores("ABC") == [1, 1, 1]

assert calculate_scores("ABCBACC") == [2, 2, 3]

