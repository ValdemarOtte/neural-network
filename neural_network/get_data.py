import random


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
            if x + y > 1:
                break
        points.append([x, y])
    return points
