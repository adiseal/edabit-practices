def pirates_killed(gold_distribution, inequality_thresholds):
    richest_pirate_gold = max(gold_distribution)
    for gold, threshold in zip(gold_distribution, inequality_thresholds):
        if richest_pirate_gold - gold > threshold:
            return True
    return False