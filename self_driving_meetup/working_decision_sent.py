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

        if ic > best_ic:
            best_ic = ic
            best_model = m
            if ic > goal_inliers and stop_at_goal:
                break
    return best_model, best_ic

# import sys
# sys.stdin = open("sdc_point_cloud.txt", "r")

delta = float(input())
n = int(input())

points = []
for i in range(0, n):
    x, y, z = input().split()
    x = float(x)
    y = float(y)
    z = float(z)
    points.append([x, y, z])

max_iterations = 100
goal_inliers = n * 0.5

# RANSAC
m, b = run_ransac(points, estimate, lambda x, y: is_inlier(x, y, delta), n, goal_inliers, max_iterations)
a, b, c, d = m
print("%f %f %f %f" % (a, b, c, d))
