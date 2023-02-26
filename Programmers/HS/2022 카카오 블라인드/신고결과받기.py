from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)

    send = defaultdict(set)
    count = defaultdict(int)

    for r in report:
        sender, receiver = r.split()
        send[sender].add(receiver)

    for receivers in send.values():
        for receiver in receivers:
            count[receiver] += 1

    for i, id in enumerate(id_list):
        for receiver in send[id]:
            if count[receiver] < k:
                continue
            answer[i] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
result = [2,1,1,0]

print(result == solution(id_list, report, k))