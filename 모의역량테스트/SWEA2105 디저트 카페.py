import sys


def search(r, c):
    global result
    if not((0 <= r < N-2) and (0 < c < N-1)):
        return
    for i in range(1, N-c):
        for j in range(1, c+1):
            if r+i+j >= N or (i+1)*(j+1) <= result:
                continue
            if calculate(r, c, i, j):
                result = max(calculate(r, c, i, j), result)


def calculate(r, c, i, j):
    cr, cc = r, c
    visited = set()
    for _ in range(i):
        cr, cc = cr+1, cc+1
        if arr[cr][cc] in visited:
            return False
        else:
            visited.add(arr[cr][cc])
    for _ in range(j):
        cr, cc = cr+1, cc-1
        if arr[cr][cc] in visited:
            return False
        else:
            visited.add(arr[cr][cc])
    for _ in range(i):
        cr, cc = cr-1, cc-1
        if arr[cr][cc] in visited:
            return False
        else:
            visited.add(arr[cr][cc])
    for _ in range(j):
        cr, cc = cr-1, cc+1
        if arr[cr][cc] in visited:
            return False
        else:
            visited.add(arr[cr][cc])
    return len(visited)


sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    result = -1
    for i in range(N):
        for j in range(N):
            search(i, j)
    print(f'#{tc}', result)