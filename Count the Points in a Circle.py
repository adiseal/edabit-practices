def points_in_circle(points, cx, cy, r):
    count = 0
    for point in points:
        x, y = point['x'], point['y']
        if (x - cx)**2 + (y - cy)**2 < r**2:
            count += 1
    return count