# https://contest.yandex.ru/contest/8458/problems/E/

import sys
sys.stdin = open("input.txt", "r")

from collections import defaultdict

n = int(input())

def_dict = defaultdict(int)
for i in range(n):
    list_str = input().split()
    for number in list_str[1:]:
        def_dict[number] += 1

print(def_dict)

for i in range(100):
    x = def_dict[str(i)]
    if x is not None:
        for j in range(x):
            print(i, end=' ')
