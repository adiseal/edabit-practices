def total_volume(*boxes):
    volume = 0
    for box in boxes:
        volume += box[0] * box[1] * box[2]
    return volume

print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1])) # 63