def filter_by_rating(d, rating):
    result = {k: v for k, v in d.items() if v == rating}
    return result if result else "No results found"
