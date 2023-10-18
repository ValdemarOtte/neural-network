from matplotlib import pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np



matrix = []
n = np.arange(0, 2, 0.1)
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

diff = float(n[1]/2)




for i, row in enumerate(matrix):
    for j, x in enumerate(row):
        points = np.array([[n[i]-diff, n[j]-diff], [n[i]-diff, n[j]+diff], [n[i]+diff, n[j]+diff], [n[i]+diff, n[j]-diff]])
        hull = ConvexHull(points)


        if matrix[i][j] == 0:
            color = "r"
        else:
            color = "b"
        plt.fill(points[hull.vertices,0], points[hull.vertices,1], color, alpha=0.3)
"""

plt.plot(0.5,0.5, "o")

plt.plot(1.5,0.5, "o")
points = np.array([[1, 0], [1, 1], [2, 1], [2, 0]])
hull = ConvexHull(points)
plt.fill(points[hull.vertices,0], points[hull.vertices,1], 'b', alpha=0.3)
"""
plt.show()
