# Задача была — выдать деньги.
# Условие минимального количества купюр не ставилось, просто выдать, но желательно максимальными купюрами.
#
# И третья итерация была с такими лимитами:
#
# var limits = {
#   5000: 4,
#   1000: 5,
#   500: 2,
#   100: 5,
#   50: 100,
#   30: 23
# };
# Здесь просто идти в лоб от наибольшего значения к наименьшему нельзя,
# т.к. в лоб я не смогу вернуть значение 120, которое можно соорудить из 30-к.
# А идти от наименьшего нельзя по условию задачи (да и не должен банкомат выдавать деньги мелкими купюрами).

# https://informatics.mccme.ru/mod/book/view.php?id=815&chapterid=59

from collections import defaultdict

limits = {
  5000: 4,
  1000: 5,
  500: 2,
  100: 5,
  50: 100,
  30: 3
}

inf = 1000000000

def cup_amount(amount):
    F = []
    F.append(0)

    a = list(limits.keys())
    a.sort()

    for i in range(1, amount + 1):
        F.append(inf)

        for j in range(0, len(a)):
            if i >= a[j] and F[i - a[j]] + 1 < F[i]:
                F[i] = F[i - a[j]] + 1

    return F


def get_money(amount):
    rez = defaultdict(int)
    F = cup_amount(amount)
    cupurs = list(limits.keys())
    cupurs.sort()

    if F[amount] == inf:
        print('Требуемую сумму выдать невозможно')
    else:
        while amount > 0:
            for i in range(len(cupurs)):
                if F[amount - cupurs[i]] == F[amount] - 1:
                    rez[cupurs[i]] += 1

                    limits[cupurs[i]] -= 1
                    if limits[cupurs[i]] < 0:
                        print(f'not enough cupur {cupurs[i]}')
                        return

                    amount -= cupurs[i]
                    break

    return rez


rez = cup_amount(120)
print(rez)
for i in range(len(rez)):
    if rez[i] != inf:
        print(i, rez[i])

rez = get_money(120)
print(rez)
