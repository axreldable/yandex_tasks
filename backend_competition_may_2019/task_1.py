# tasks
# https://contest.yandex.ru/contest/12870/problems/

import sys
sys.stdin = open("input.txt", "r")

def dots_amount(high, x, ni):
    return (high - ni) // x + 1

n, x, k = input().split()
n = int(n)
x = int(x)
k = int(k)
tasks = input().split()
tasks_int = []
for task in tasks:
    tasks_int.append(int(task))
tasks_int.sort()

# print(n, x, k)
# print(tasks_int)

tasks_set = set()

start = tasks_int[0]
while 1:
    tasks_set = set()
    for ni in tasks_int:
        z = dots_amount(start, x, ni)
        for i in range(0, z):
            tasks_set.add(ni + i * x)
    if len(tasks_set) >= k:
        one_ar = list(tasks_set)
        one_ar.sort()

        # print(one_ar)

        print(one_ar[k - 1])
        break
    start = start + 10
