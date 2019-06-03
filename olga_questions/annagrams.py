# getAnagrams(“нос”, “сон”, “снедь”, “днесь”)
#
# Должна вернуть
#
# [
#   ["нос", "сон"],
#   ["днесь", "снедь"]
# ]
from collections import defaultdict


def def_dict(word):
    rez = defaultdict(int)

    for c in list(word):
        rez[c] += 1

    return rez


def is_anagram(first, second):
    return def_dict(first) == def_dict(second)


def get_anagrams_base(word, words):
    rez = []
    for w in words:
        if is_anagram(word, w):
            rez.append([w, word])
    return rez


def get_anagrams(prev, words):
    if len(words) == 0:
        return prev

    for an in get_anagrams_base(words[0], words[1:]):
        prev.append(an)

    return get_anagrams(prev, words[1:])


print(get_anagrams([], ["нос", "сон", "снедь", "днесь", "ндесь"]))
# [['сон', 'нос'], ['днесь', 'снедь'], ['ндесь', 'снедь'], ['ндесь', 'днесь']]
