# https://contest.yandex.ru/contest/8458/problems/?nc=Eoqq2kRp

import sys
sys.stdin = open("input.txt", "r")

jewels = input()
stones = input()

counter = 0
for s in stones:
    if s in jewels:
        counter += 1

print(counter)
