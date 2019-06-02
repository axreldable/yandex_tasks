# https://contest.yandex.ru/contest/8458/problems/C/

import sys
sys.stdin = open("input.txt", "r")

n = int(input())

if n == 0:
    exit(0)

if n == 1:
    print(input())
    exit(0)

current = input()
next = current
for i in range(0, n - 1):
    next = input()
    if next != current:
        print(current)
        current = next

if next == current:
    print(current)
