# Написать функцию getPrimes(n) // Должна вернуть простые числа от 2 до n;
import math


# ------------------ O(n^2) ---------------------
import time


def is_prime_1(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_primes_1(n):  # 100_000: ms: 33825.98304748535
    for i in range(2, n):
        if is_prime_1(i):
            x = 1
            # print(i, end=' ')


# ------------------ O(n*n^(1/2)) ---------------------
def is_prime_2(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def get_primes_2(n):  # 100_000: ms: 204.98108863830566
    for i in range(2, n):
        if is_prime_2(i):
            x = 1
            # print(i, end=' ')


# ------------------ O(n*log(log(n))) ---------------------
def eratosthenes(n):     # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve


def get_primes_3(n):  # 100_000: ms: 41.05019569396973
    for i in eratosthenes(n):
        if i != 0:
            x = 1
            # print(i, end=' ')


start_time = time.time()
get_primes_3(100_000)
spend_time = time.time() - start_time
print()
print(f'ms: {spend_time * 1000}')
