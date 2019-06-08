# Задача была — выдать деньги.
# Условие минимального количества купюр не ставилось, просто выдать, но желательно максимальными купюрами.

# Вторая итерация задачи включала лимиты:
#
# var limits = {
#   5000: 4,
#   1000: 5,
#   500: 2,
#   100: 5,
#   50: 100
# };
# function getMoney(amount, limits) {
#    // нужно вернуть набор денег и обновленные лимиты
#    // {
#    //   res: {
#    //     5000: 1,
#    //     1000: 2,
#    //     ....
#    //     50: 5
#    //   } || "warn" (если вернуть деньги невозможно)
#    //  limits: // объект лимитов той же структуры с обновленными    данными
#    // }
# }
from collections import defaultdict

limits = {
  5000: 4,
  1000: 5,
  500: 2,
  100: 5,
  50: 100
}


def get_money(amount):
    rez_dict = defaultdict(int)

    for cur_cup in limits.keys():
        while amount - cur_cup >= 0:
            if limits[cur_cup] == 0:
                break
            limits[cur_cup] -= 1

            rez_dict[cur_cup] += 1

            amount = amount - cur_cup

    if amount != 0:
        raise RuntimeError(f'Failed to give rest {amount}, limits={limits}')

    return {
        'res': rez_dict,
        'limits': limits
    }


rez = get_money(150000)
print(rez)
