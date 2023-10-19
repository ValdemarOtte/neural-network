import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial import ConvexHull


def draw_background_color(matrix: list[int], n: np.array) -> None:
    """
    Draw the backgroundcolor of the areals where the nn thinks if 0, 1 or 2.

    Args:
    ----
        matrix: The matrix with 0, 1 or 2 after whichs (x,y) nn thinks is
        n: numpy arange
    """
    diff = float(n[1] / 2)

    for i, row in enumerate(matrix):
        print(f"{i}/{len(matrix)}")
        for j, _ in enumerate(row):
            points = np.array(
                [
                    [n[i] - diff, n[j] - diff],
                    [n[i] - diff, n[j] + diff],
                    [n[i] + diff, n[j] + diff],
                    [n[i] + diff, n[j] - diff],
                ],
            )
            hull = ConvexHull(points)

            if matrix[i][j] == 0:
                color = "r"
            if matrix[i][j] == 1:
                color = "b"
            if matrix[i][j] == 2:
                color = "g"
            # else:
            #    color = "y"
            plt.fill(points[hull.vertices, 0], points[hull.vertices, 1], color, alpha=0.3)


def draw_points(points: list[list[float]], color: str) -> None:
    for point in points:
        plt.plot(
            point[0],
            point[1],
            marker="o",
            markeredgecolor=color,
            markerfacecolor=color,
        )


def draw(points: list[list[list[float]]], matrix: list[list[int]]) -> None:
    """
    Draw a matplot of points.

    Args:
    ----
        points: A list of list of points which need to be blue or red
        matrix: A list of points which need to be red

    """
    # Matplotlib style
    plt.style.use("ggplot")

    # Fix size of drawing to fit all points with a border of 1
    plt.xlim(-1, 3)
    plt.ylim(-1, 3)

    # Draw points
    draw_points(points[0], "#3c40c6")  # Blue
    draw_points(points[1], "#ff3f34")  # Red

    # Draw background color
    n = np.arange(0, 2, 0.05)
    draw_background_color(matrix, n)

    # Show drawing
    plt.show()
