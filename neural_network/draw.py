from matplotlib import pyplot as plt
import numpy as np

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


"""
x = np.arange(-1, 21, 0.1)
a = 8 + 1 * x
a2 = 16 - 1 * x

plt.plot(x, a)

#x = np.arange(0.0, 2, 0.01)
plt.xlim(-1, 21)
plt.ylim(-1, 21)

plt.fill_between(x, x, 0)

n = np.arange(0, 3, 0.1)

matrix = []

for i, y in enumerate(n):
    matrix.append([])
    for x in n:
        if x < 1 and y < 1:
            value = 0
        else:
            value = 1
        matrix[i].append(str(value))

for row in matrix:
    print("".join(row))
"""


"""
from scipy.spatial import ConvexHull
points = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print(type(points))
hull = ConvexHull(points)
plt.fill(points[hull.vertices,0], points[hull.vertices,1], 'r', alpha=0.3)

points = np.array([[1, 0], [1, 1], [2, 0], [2, 1]])



hull = ConvexHull(points)
plt.fill(points[hull.vertices,0], points[hull.vertices,1], 'k', alpha=0.3)
plt.show()

"""


matrix = []
n = np.arange(0, 3, 0.1)
for i, y in enumerate(n):
    matrix.append([])
    for x in n:
        if x < 1 and y < 1:
            value = 0
        else:
            value = 1
        matrix[i].append(str(value))

for row in matrix:
    print("".join(row))


coordinats = []
seen = []
target = 0
x = 0
y = 0
data = {
    "0": [],
    "1": []
}

import 

def find_hull(target, x, y, coordinats, seen):

    try:
        if matrix[y][x + 1] == target and [y, x + 1] not in coordinats and [y, x + 1] not in seen:
            coordinats.append([y, x + 1])
            seen.append([y, x + 1])
            find_hull(target, x + 1, y, coordinats, seen)
    except IndexError:
        pass

    try:
        if matrix[y][x - 1] == target and [y, x - 1] not in coordinats and [y, x - 1] not in seen:
            coordinats.append([y, x - 1])
            seen.append([y, x - 1])
            find_hull(target, x - 1, y, coordinats, seen)
    except IndexError:
        pass


    try:
        if matrix[y + 1][x] == target and [y + 1, x] not in coordinats and [y + 1, x] not in seen:
            coordinats.append([y + 1, x])
            seen.append([y + 1, x])
            find_hull(target, x, y + 1, coordinats, seen)
    except IndexError:
        pass
    try:
        if matrix[y - 1][x] == target and [y - 1, x] not in coordinats and [y - 1, x] not in seen:
            coordinats.append([y - 1, x])
            seen.append([y - 1, x])
            find_hull(target, x, y - 1, coordinats, seen)
    except IndexError:
        pass
    """
    try:
        if matrix[y + 1][x + 1] == target and [y + 1, x + 1] not in coordinats and [y + 1, x + 1] not in seen:
            coordinats.append([y + 1, x + 1])
            seen.append([y + 1, x + 1])
            find_hull(target, x + 1, y + 1, coordinats, seen)
    except IndexError:
        pass
    """
    return coordinats, seen


matrix.reverse()
for y, row in enumerate(matrix):
    for x, element in enumerate(row):
        coordinats = []
        if [y, x] not in seen:
            seen.append([y, x])
            coordinats.append([y, x])
            target = element
            coordinats, seen = find_hull(target, y, x, coordinats, seen)
            data[str(target)].append(coordinats)

print(len(data["1"]))
print(data["1"])
from scipy.spatial import ConvexHull
points = np.array(data["0"][0])
"""

hull = ConvexHull(points)
plt.fill(points[hull.vertices,0], points[hull.vertices,1], 'r', alpha=0.3)


points = np.array(data["1"][0])
hull = ConvexHull(points)
plt.fill(points[hull.vertices,0], points[hull.vertices,1], 'r', alpha=0.3)


points = np.array(data["1"][0])

hull = ConvexHull(points)
plt.fill(points[hull.vertices,0], points[hull.vertices,1], 'k', alpha=0.3)
"""


plt.xlim(0, 7)
plt.ylim(0, 4)
plt.show()
