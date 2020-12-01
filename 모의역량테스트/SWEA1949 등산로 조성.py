from collections import deque
import sys


def search(row, col):
    global result
    q = deque()
    visit = list()
    visit.append((row, col))
    q.append((row, col, arr[row][col], False, visit, 1))
    while q:
        cr, cc, height, shape, visited, total = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = cr+dr, cc+dc
            if (0 <= nr < N) and (0 <= nc < N) and (nr, nc) not in visited:
                if arr[nr][nc] < height:
                    q.append((nr, nc, arr[nr][nc], shape, visited+[(nr, nc)], total+1))
                    continue
                if not shape and arr[nr][nc]-K < height:
                    q.append((nr, nc, height-1, True, visited+[(nr, nc)], total+1))
    result = max(result, total)


sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    find_max = 0
    for i in range(N):
        find_max = max(max(arr[i]), find_max)

    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == find_max:
                search(i, j)
    print(f'#{tc}', result)