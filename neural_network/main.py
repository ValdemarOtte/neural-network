import random
from matplotlib import pyplot as plt


def create_random_points_blue(min_: int, max_: int, n: int) -> list[list[float]]:
    """
    Create random blue points.

    Args:
    ----
        min_: Minimum for the value of the point
        max_: Maxsimun for the value of the point
        n: Number of points which need to be created

    Returns:
    -------
        A list of random created points
    """
    points = []
    for _ in range(n):
        x = round(random.uniform(min_, max_), 2)  # noqa: S311
        y = round(random.uniform(min_, (max_ - x)), 2)  # noqa: S311
        points.append([x, y])
    return points


def create_random_points_red(min_: int, max_: int, n: int) -> list[list[float]]:
    """
    Create random red points.

    Args:
    ----
        min_: Minimum for the value of the point
        max_: Maxsimun for the value of the point
        n: Number of points which need to be created

    Returns:
    -------
        A list of random created points
    """
    points = []
    for _ in range(n):
        while True:
            x = round(random.uniform(min_, max_), 2)  # noqa: S311
            y = round(random.uniform(min_, max_), 2)  # noqa: S311
            if x + y > 8:
                break
        points.append([x, y])
    return points


if __name__ == "__main__":
    points_blue = create_random_points_blue(0, 8, 20)
    points_red = create_random_points_red(0, 20, 80)
    points = points_blue + points_red

    for point in points_blue:
        plt.plot(point[0], point[1], marker="o", markeredgecolor="blue", markerfacecolor="blue")
    for point in points_red:
        plt.plot(point[0], point[1], marker="o", markeredgecolor="red", markerfacecolor="red")
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.show()