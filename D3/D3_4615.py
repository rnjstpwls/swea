import sys
sys.stdin = open('input.txt', 'r')

def around_search(x, y, color):
    find_color = 3 - color
    for i in range(8):
        if not (0 <= y + dr[i] < N) or not (0 <= x + dc[i] < N):
            continue
        if board[y + dr[i]][x + dc[i]] == find_color:
            change_color(x, y, i, color)
    return


def change_color(x, y, i, color):
    stack = []
    cnt = 1
    while True:
        if not (0 <= y + dr[i] * cnt < N) or not (0 <= x + dc[i] * cnt < N):
            return
        if board[y + dr[i] * cnt][x + dc[i] * cnt] == 0:
            return
        if board[y + dr[i] * cnt][x + dc[i] * cnt] == color:
            break
        stack.append((x + dc[i] * cnt, y + dr[i] * cnt, board[y + dr[i] * cnt][x + dc[i] * cnt]))
        cnt += 1

    for i in range(len(stack)):
        board[stack[i][1]][stack[i][0]] = color
    return


def stone_counter(color):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == color:
                cnt += 1
    return cnt


def show_board():
    for row in board:
        print(*row)
    print()

# 1 흑돌 2 백돌
# 위에서부터 시계방향
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # board판 생성 및 초기화
    board = [[0] * N for _ in range(N)]
    board[N // 2][N // 2], board[N // 2 - 1][N // 2 - 1] = 2, 2
    board[N // 2 - 1][N // 2], board[N // 2][N // 2 - 1] = 1, 1

    for _ in range(M):
        x, y, color = map(int, input().split())
        board[y - 1][x - 1] = color
        around_search(x - 1, y - 1, color)
        # show_board()

    black = stone_counter(1)
    white = stone_counter(2)

    print(f'#{tc}', black, white)