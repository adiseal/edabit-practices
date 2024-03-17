def record_temps(records, current_week):
    for i in range(7):  
        if current_week[i][0] < records[i][0]:
            records[i][0] = current_week[i][0]
        if current_week[i][1] > records[i][1]:
            records[i][1] = current_week[i][1]
    return records