# https://contest.yandex.ru/contest/8458/problems/E/

import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")

first = input()
second = input()

first_dict = defaultdict(int)
for c in first:
    first_dict[c] += 1

second_dict = defaultdict(int)
for c in second:
    second_dict[c] += 1


# print(first_dict)
# print(second_dict)

if first_dict == second_dict:
    print(1)
else:
    print(0)
