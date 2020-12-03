import copy
import sys
from collections import deque


def bomb(r, c, arr):
    q = deque()
    visited = set()
    q.append((r, c))
    visited.add((r, c))
    while q:
        cr, cc = q.popleft()
        size = arr[cr][cc] - 1
        for s in range(1, size + 1):
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = cr + dr * s, cc + dc * s
                if (0 <= nr < H) and (0 <= nc < W) and (nr, nc) not in visited:
                    q.append((nr, nc))
                    visited.add((nr, nc))

    for col in range(W):
        tmp = []
        for row in range(H):
            if arr[H - row - 1][col] > 0 and (H - row - 1, col) not in visited:
                tmp.append(arr[H - row - 1][col])
            elif arr[H - row - 1][col] == 0:
                break
        for i in range(len(tmp)):
            arr[H - i - 1][col] = tmp[i]
        for i in range(H - len(tmp)):
            arr[i][col] = 0


def select_column(col, arr):
    for row in range(H):
        if arr[row][col]:
            return row
    return -1


def block_cnt(arr):
    cnt = 0
    for r in range(H):
        for c in range(W):
            if arr[r][c]:
                cnt += 1
    return cnt


def search(cnt, ori_arr):
    global result

    if cnt == N:
        result = min(result, block_cnt(ori_arr))
        return

    for i in range(W):
        sr = select_column(i, ori_arr)
        tmp_arr = copy.deepcopy(ori_arr)
        if sr == -1:
            search(cnt + 1, tmp_arr)
        else:
            bomb(sr, i, tmp_arr)
            search(cnt + 1, tmp_arr)


sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(H))

    result = float('inf')
    search(0, arr)
    print(f'#{tc}', result)
