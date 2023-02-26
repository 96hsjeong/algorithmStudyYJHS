max_sheep = 0

def solution(info, edges):
    n = len(info)
    graph = [[] for _ in range(n)]
    visited = [0] * (2 ** n)

    for from_, to_ in edges:
        graph[from_].append(to_)
        graph[to_].append(from_)

    check(n, info, graph, visited, 1 << 0, 0, 0, 0)
    return max_sheep


def check(n, info, graph, visited, visit, current, sheep, wolf):
    global max_sheep

    if info[current]:
        wolf += 1
    else:
        sheep += 1

    if sheep <= wolf or visited[visit]:
        return

    max_sheep = max(max_sheep, sheep)
    visited[current] = 1

    for i in range(n):
        if not visit & 1 << i:
            continue
        for next in graph[i]:
            if visit & 1 << next:
                continue
            check(n, info, graph, visited, visit | 1 << next, next, sheep, wolf)


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
result = 5

print(result == solution(info, edges))