from matplotlib import pyplot as plt


def draw(points_blue: list[list[float]], points_red: list[list[float]]) -> None:
    """
    Draw a matplot of points.

    Args:
    ----
        points_blue: A list of points which need to be blue
        points_blue: A list of points which need to be red

    """
    # Matplotlib style
    plt.style.use("ggplot")

    # Fix size of drawing to fit all points with a border of 1
    plt.xlim(-1, 21)
    plt.ylim(-1, 21)

    # Draw points
    for point in points_blue:
        plt.plot(
            point[0],
            point[1],
            marker="o",
            markeredgecolor="#3c40c6",
            markerfacecolor="#3c40c6",
        )
    for point in points_red:
        plt.plot(
            point[0],
            point[1],
            marker="o",
            markeredgecolor="#ff3f34",
            markerfacecolor="#ff3f34",
        )

    # Show drawing
    plt.show()
