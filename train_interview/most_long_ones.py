# https://contest.yandex.ru/contest/8458/problems/B/

import sys
sys.stdin = open("input.txt", "r")

n = int(input())

current = 0
max_c = 0
for i in range(0, n):
    x = input()
    if x == '1':
        current += 1
    else:
        max_c = max(max_c, current)
        current = 0

max_c = max(max_c, current)
print(max_c)
