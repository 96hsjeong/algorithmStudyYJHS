from collections import deque

d = [(-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd')]


def solution(n, m, x, y, r, c, k):
    min_d = calc_distance(x, y, r, c)

    if k < min_d or (k - min_d) % 2:
        return "impossible"

    stack = deque([(x, y, '')])

    while stack:
        x, y, path = stack.pop()

        if x == r and y == c and len(path) == k:
            return path

        for dx, dy, direction in d:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, n, m) and calc_distance(nx, ny, r, c) + len(path) < k:
                stack.append((nx, ny, path + direction))


def in_range(x, y, n, m):
    if 1 <= x <= n and 1 <= y <= m:
        return True
    return False


def calc_distance(x, y, r, c):
    return abs(r - x) + abs(c - y)


n, m, x, y, r, c, k = 3, 4, 2, 3, 3, 1, 5
result = "dllrl"

print(result == solution(n, m, x, y, r, c, k))

n, m, x, y, r, c, k = 3, 3, 1, 2, 3, 3, 4
result = "impossible"

print(result == solution(n, m, x, y, r, c, k))

