import sys
sys.stdin = open("input_3.txt", "r")

k, n = input().split()
n = int(n)
k = int(k)
cards = input().split()
cards_int = []
for card in cards:
    cards_int.append(int(card))

# print(k, n)
# print(cards_int)

# max = 10 ** 7 + 8
max = 10

score = 1
score_v = 0
score_p = 0

next_ar = cards_int
while max:
    ar = []
    for i in next_ar:
        if i % 17 == 0 and i % 31 == 0:
           ar.append(i)
           continue
        elif i % 17 == 0:
            score_v += score
            if score_v == k:
                print('Vasya')
                exit(0)
        elif i % 31 == 0:
            score_p += score
            if score_p == k:
                print('Petya')
                exit(0)
    max = max - 1
    score *= 2
    next_ar = ar

print('Too long')
