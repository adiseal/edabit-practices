def upload_count(dates, month):
    count = 0
    for date in dates:
        if date.startswith(month):
            count += 1
    return count

print(upload_count(["Sept 22", "Sept 21", "Oct 15"], "Sept")) # 2
print(upload_count(["Sept 22", "Sept 21", "Oct 15"], "Oct")) # 1