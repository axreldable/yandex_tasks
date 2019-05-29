import random
import numpy as np

def augment(xyzs):
    axyz = np.ones((len(xyzs), 4))
    axyz[:, :3] = xyzs
    return axyz

def estimate(xyzs):
    axyz = augment(xyzs[:3])
    return np.linalg.svd(axyz)[-1][-1, :]

def is_inlier(coeffs, xyz, threshold):
    return np.abs(coeffs.dot(augment([xyz]).T)) < threshold

def run_ransac(data, estimate, is_inlier, sample_size, goal_inliers, max_iterations, stop_at_goal=True, random_seed=None):
    best_ic = 0
    best_model = None
    random.seed(random_seed)
    # random.sample cannot deal with "data" being a numpy array
    for i in range(max_iterations):
        s = random.sample(data, int(sample_size))
        m = estimate(s)
        ic = 0
        for j in range(len(data)):
            if is_inlier(m, data[j]):
                ic += 1

        print(s)
        print('estimate:', m,)
        print('# inliers:', ic)

        if ic > best_ic:
            best_ic = ic
            best_model = m
            if ic > goal_inliers and stop_at_goal:
                break
    print('took iterations:', i+1, 'best model:', best_model, 'explains:', best_ic)
    return best_model, best_ic

import sys
sys.stdin = open("input.txt", "r")
sys.stdin = open("sdc_point_cloud.txt", "r")

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

print('xs', xs)
print('ys', ys)
print('zs', zs)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs, color='b')
# plt.show()

max_iterations = 100
goal_inliers = n * 0.5

# RANSAC
m, b = run_ransac(points, estimate, lambda x, y: is_inlier(x, y, delta), n, goal_inliers, max_iterations)
a, b, c, d = m

f0 = - a / c
f1 = - b / c
f2 = - d / c

# plot plane
xlim = ax.get_xlim()
ylim = ax.get_ylim()
X,Y = np.meshgrid(np.arange(xlim[0], xlim[1]),
                  np.arange(ylim[0], ylim[1]))
Z = np.zeros(X.shape)
for r in range(X.shape[0]):
    for c in range(X.shape[1]):
        Z[r,c] = f0 * X[r,c] + f1 * Y[r,c] + f2
ax.plot_wireframe(X,Y,Z, color='k')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
