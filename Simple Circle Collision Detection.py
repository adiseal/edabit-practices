def is_circle_collision(circle1, circle2):
    distance = ((circle1[1] - circle2[1])**2 + (circle1[2] - circle2[2])**2)**0.5
    if distance <= (circle1[0] + circle2[0]):
        return True
    else:
        return False
