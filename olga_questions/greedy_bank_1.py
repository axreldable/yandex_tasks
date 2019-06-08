# Задача была — выдать деньги.
# Условие минимального количества купюр не ставилось, просто выдать, но желательно максимальными купюрами.

# var moneyTypes = [5000, 1000, 500, 100, 50];
# function getMoney(amount) {
#    // нужно вернуть набор денег в следующем формате
#    // {
#    //   5000: 1,
#    //   1000: 2,
#    //   ....
#    //   50: 5
#    // }
#    // Или бросить исключение, если вернуть деньги невозможно
# }
from collections import defaultdict

money_types = [5000, 1000, 500, 100, 50]


def get_money(amount):
    rez_dict = defaultdict(int)

    for cur_cup in money_types:
        while amount - cur_cup >= 0:
            rez_dict[cur_cup] += 1
            amount = amount - cur_cup

    if amount != 0:
        raise RuntimeError(f'Failed to give rest {amount}')

    return rez_dict


rez = get_money(150)
print(rez)
