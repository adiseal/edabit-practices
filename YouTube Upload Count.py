def upload_count(dates, month):
    count = 0
    for date in dates:
        if date.startswith(month):
            count += 1
    return count
