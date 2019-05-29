import numpy as np

import sys
sys.stdin = open("input.txt", "r")

delta = float(input())
n = int(input())

points = []
for i in range(0, n):
    x, y, z = input().split()
    x = float(x)
    y = float(y)
    z = float(z)
    points.append([x, y, z])

# print('delta', delta)
# print('n', n)
# print('points', points)

xs = []
ys = []
zs = []
for point in points:
    xs.append(point[0])
    ys.append(point[1])
    zs.append(point[2])

# do fit
tmp_A = []
tmp_b = []
for i in range(len(xs)):
    tmp_A.append([xs[i], ys[i], 1])
    tmp_b.append(zs[i])
b = np.matrix(tmp_b).T
A = np.matrix(tmp_A)
fit = (A.T * A).I * A.T * b
errors = b - A * fit
residual = np.linalg.norm(errors)

# print("%f x + %f y + %f = z" % (fit[0], fit[1], fit[2]))

c = 1
a = - fit[0] * c
b = - fit[1] * c
d = - fit[2] * c
# print("%f x + %f y + %f z + %f = 0" % (a, b, c, d))
print("%f %f %f %f" % (a, b, c, d))
