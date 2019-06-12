# https://code.yandex-team.ru/f94722ff-006b-4f94-9eac-98e2498b804b


# == 1 ==
# s = "123"
# f(s) -> "124"
def inc(str_num):
    if str_num == '':
        return 1
    without_last = str_num[:-1]
    last_num = int(str_num[-1:])
    if last_num < 9:
        n = last_num + 1
        return without_last + str(n)
    else:
        return inc(without_last) + '0'


print(inc('1211111111111111111111111113'))


# == 2 ==
# [(x, y), ...]
# вертикальная ось симметрии

def is_simm(ar):
    # from collections import defaultdict
    # dict_y = defaultdict([])
    # dict_y[y].append(x)
    dict_y = {}
    for point in ar:  # for x, y in ar:
        x = point[0]
        y = point[1]
        ar_x = dict_y(y)
        if ar_x is None:
            dict_y.put(y, [x])  # dict_y[y] = [x]
        else:
            dict_y.put(y, ar_x.append(x))  # dict_y[y].append(x)
    # dict_y: {y: [x, ...]}
    m = 0
    is_first = True
    for (y, ar_x) in dict_y:
        ar_sort = sort(ar_x)  # ar_sort = None, нужно sorted()
        for i in range(0, len(ar_x) / 2):
            if is_first:
                m = (ar_sort[i] + ar_sort[len(ar_x) - 1 - i]) / 2
            else:
                m1 = (ar_sort[i] + ar_sort[len(ar_x) - 1 - i]) / 2
                if m1 != m:
                    return False
        if len(ar_x) % 2 != 0:
            if ar_x[len(ar_x) / 2] != m:
                return False

    return True