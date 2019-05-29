import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

print('delta', delta)
print('n', n)
print('points', points)

xs = []
ys = []
zs = []
for point in points:
    xs.append(point[0])
    ys.append(point[1])
    zs.append(point[2])

print('xs', xs)
print('ys', ys)
print('zs', zs)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs, color='b')
# plt.show()

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

print(fit)
print("solution:")
print("%f x + %f y + %f = z" % (fit[0], fit[1], fit[2]))
print("errors:")
print(errors)
print("residual:")
print(residual)

# plot plane
xlim = ax.get_xlim()
ylim = ax.get_ylim()
X,Y = np.meshgrid(np.arange(xlim[0], xlim[1]),
                  np.arange(ylim[0], ylim[1]))
Z = np.zeros(X.shape)
for r in range(X.shape[0]):
    for c in range(X.shape[1]):
        Z[r,c] = fit[0] * X[r,c] + fit[1] * Y[r,c] + fit[2]
ax.plot_wireframe(X,Y,Z, color='k')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

c = 1
a = - fit[0] * c
b = - fit[1] * c
d = - fit[2] * c
print("%f x + %f y + %f z + %f = 0" % (a, b, c, d))
