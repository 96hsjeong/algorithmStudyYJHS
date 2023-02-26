N, M = -1, -1


def solution(board, skill):
    global N, M

    N, M = len(board), len(board[0])
    temp = [[0] * (M + 1) for _ in range(N + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree
        play(temp, r1, c1, r2 + 1, c2 + 1, degree)

    temp = make_mask(temp)
    put_mask(board, temp)
    answer = check(board)

    return answer


def play(temp, r1, c1, r2, c2, degree):
    temp[r1][c1] += degree
    temp[r1][c2] += -degree
    temp[r2][c1] += -degree
    temp[r2][c2] += degree


def make_mask(temp):
    for i in range(N):
        for j in range(M + 1):
            temp[i+1][j] += temp[i][j]

    for i in range(N + 1):
        for j in range(M):
            temp[i][j+1] += temp[i][j]

    return temp


def put_mask(board, temp):
    for i in range(N):
        for j in range(M):
            board[i][j] += temp[i][j]


def check(board):
    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] <= 0:
                continue
            count += 1
    return count


board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
result = 10
result = 6
print(result == solution(board, skill))