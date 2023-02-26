max_diff = 1
lion_info = [0] * 11
answer = [-1]


def solution(n, info):
    get_score(n, info, 0, 0, 0)
    return answer


def get_score(n, apeach_info, idx, apeach, lion):
    global max_diff, lion_info, answer

    # 과녁 점수가 0점인 경우
    if idx == 10:
        # 라이언의 남은 화살을 0점에...
        lion_info[idx] = n

        # 라이언과 어피치의 점수 차이가 최대 차이 보다 큰 경우
        if max_diff < lion - apeach or (max_diff > 0 and max_diff == lion - apeach and check()):
            # 최대 차이 갱신
            max_diff = lion - apeach
            # 정답 갱신
            answer = lion_info[:]

        return

    # 과녁 점수
    score = 10 - idx

    lion_info[idx] = 0

    if apeach_info[idx] == 0:
        # 둘 다 점수 획득 못하는 경우
        get_score(n, apeach_info, idx + 1, apeach, lion)
    else:
        # 어피치가 점수 획득하는 경우
        get_score(n, apeach_info, idx + 1, apeach + score, lion)

    count = apeach_info[idx] + 1

    if count <= n:
        # 어피치 보다 한발 더 맞춤
        lion_info[idx] = count
        # 라이언이 점수 획득하는 경우
        get_score(n - count, apeach_info, idx + 1, apeach, lion + score)


def check():
    if answer == [-1]:
        return True

    for i in range(10, -1, -1):
        if answer[i] == lion_info[i]:
            continue
        elif answer[i] < lion_info[i]:
            return True
        else:
            return False

    return False
