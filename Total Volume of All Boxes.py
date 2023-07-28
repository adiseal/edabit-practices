def total_volume(*boxes):
    volume = 0
    for box in boxes:
        volume += box[0] * box[1] * box[2]
    return volume
