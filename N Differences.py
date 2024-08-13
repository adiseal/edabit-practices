def n_differences(arr):
    while len(arr) > 1:
        arr = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    return arr[0]