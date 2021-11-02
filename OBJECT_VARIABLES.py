# Tree
def get_coordinates():
    coordinates = []
    y = 390
    for i in range(430, 550):
        if y > 510:
            y = 390
        coordinates.append((i, y))
        
    return coordinates 