def reverse_image(image):
    return [[1 - pixel for pixel in row] for row in image]