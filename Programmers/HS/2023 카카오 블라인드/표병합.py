parent = [i for i in range(50 * 50)]
table = [0] * (50 * 50)


def solution(commands):
    answer = []

    for command in commands:
        command = command.split()
        execute(answer, command)

    return answer


def execute(answer, command):
    cmd = command[0]
    if cmd == "UPDATE":
        if len(command) == 4:
            r, c, value = command[1:]
            update1(r, c, value)
        else:
            value1, value2 = command[1:]
            update2(value1, value2)
    elif cmd == "MERGE":
        r1, c1, r2, c2 = command[1:]
        merge(r1, c1, r2, c2)
    elif cmd == "UNMERGE":
        r, c = command[1:]
        unmerge(r, c)
    elif cmd == "PRINT":
        r, c = command[1:]
        p = print_(r, c)
        answer.append(p)


def update1(r, c, value):
    idx = convert_index(r, c)
    parent_idx = parent[idx]
    for i, p in enumerate(parent):
        if p == parent_idx:
            table[i] = value


def update2(value1, value2):
    for i, v in enumerate(table):
        if v == value1:
            table[i] = value2


def merge(r1, c1, r2, c2):
    idx1 = convert_index(r1, c1)
    idx2 = convert_index(r2, c2)

    if idx1 == idx2:
        return

    if table[idx1]:
        union(idx1, idx2)
    else:
        union(idx2, idx1)


def unmerge(r, c):
    idx = convert_index(r, c)
    parent_idx = parent[idx]
    for i, p in enumerate(parent):
        if p == parent_idx:
            parent[i] = i
            if i != idx:
                table[i] = 0


def print_(r, c):
    idx = convert_index(r, c)
    return table[idx] if table[idx] != 0 else "EMPTY"


def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    renew(root_a, root_b)


def renew(a, b):
    for i, p in enumerate(parent):
        if p == b:
            parent[i] = a
            table[i] = table[a]


def convert_index(r, c):
    return (int(r) - 1) * 50 + (int(c) - 1)


commandes = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
result = ["EMPTY", "group"]

print(result == solution(commandes))