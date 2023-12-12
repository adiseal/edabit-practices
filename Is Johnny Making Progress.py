def progress_days(runs):
    return sum([1 for i in range(1, len(runs)) if runs[i] > runs[i-1]])
