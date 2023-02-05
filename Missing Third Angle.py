def missing_angle(angle1, angle2):
    third_angle = 180 - (angle1 + angle2)
    if third_angle > 90 and third_angle < 180:
        return "obtuse"
    elif third_angle < 90:
        return "acute"
    elif third_angle == 90:
        return "right"
    