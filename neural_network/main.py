import numpy as np
from draw import draw  # type: ignore
from get_data import create_random_points_blue, create_random_points_red  # type: ignore

matrix = []
n = np.arange(0, 2, 0.05)
for i, y in enumerate(n):
    matrix.append([])
    for x in n:
        if x < 1 and y < 1:
            value = 0
        elif x * y < 1:
            value = 1
        else:
            value = 0
        matrix[i].append(value)


if __name__ == "__main__":
    points_blue = create_random_points_blue(0, 1, 20)
    points_red = create_random_points_red(0, 2, 80)
    points = [points_blue, points_red]

    draw(points, matrix)
