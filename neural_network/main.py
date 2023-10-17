import random


def create_random_points(min_: int, max_: int, n: int) -> list[list[float]]:
    """
    Create random points.

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


if __name__ == "__main__":
    points_blue = create_random_points(0, 5, 20)
    points_red = create_random_points(5, 20, 80)
    points = points_blue + points_red
