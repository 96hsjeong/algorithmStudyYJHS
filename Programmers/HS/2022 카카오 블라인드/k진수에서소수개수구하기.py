from collections import deque
import math


def solution(n, k):
    answer = 0
    convert_n = convert(n, k)
    numbers = list(str(convert_n).split('0'))

    for number in numbers:
        if not number:
            continue

        if is_prime(int(number)):
            answer += 1

    return answer


def convert(n, k):
    result = deque()

    while n != 0:
        n, mod = divmod(n, k)
        result.appendleft(mod)

    return ''.join(map(str, result))


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return False

    return True