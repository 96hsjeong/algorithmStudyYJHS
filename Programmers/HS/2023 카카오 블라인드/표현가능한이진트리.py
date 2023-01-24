def solution(numbers):
    answer = []

    for number in numbers:
        tree = list(map(int, bin(number)[2:]))
        n = len(tree)

        tree.reverse()
        tree.extend([0] * (len(tree) - 1))

        possible = 0

        for mid in range(n // 2, n):
            if tree[mid]:
                if check(0, 2 * mid, tree, 1):
                    possible = 1
                    break

        answer.append(possible)

    return answer


def check(start, end, tree, state):
    # 트리의 노드 개수가 홀수가 아닌 경우
    if (end - start) % 2 == 1:
        return False

    # 리프 노드인 경우
    if start == end:
        if not state and tree[start]:
            return False
        return True

    mid = (start + end) // 2

    if tree[mid]:
        if state:
            return check(start, mid - 1, tree, 1) and check(mid + 1, end, tree, 1)
        else:
            return False
    else:
        return check(start, mid - 1, tree, 0) and check(mid + 1, end, tree, 0)


numbers = [7, 42, 5]
result = [1, 1, 0]
print(result == solution(numbers))
