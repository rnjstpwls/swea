from collections import deque


def search(row, col):
    q = deque([(row, col, 1)])

    while q:
        cr, cc, time = q.popleft()
        for dr, dc in direction[arr[cr][cc]]:
            nr, nc = cr + dr, cc + dc
            if not (0 <= nr < N) or not (0 <= nc < M) or not arr[nr][nc] or not check(nr, nc, cr, cc) or (
                    nr, nc) in visited or time >= L:
                continue
            q.append((nr, nc, time + 1))
            visited.add((nr, nc))


def check(nr, nc, cr, cc):
    for dr, dc in direction[arr[nr][nc]]:
        tmpr, tmpc = nr + dr, nc + dc
        if (tmpr, tmpc) == (cr, cc):
            return True

    return False


direction = {
    1: [(-1, 0), (0, 1), (1, 0), (0, -1)], 2: [(-1, 0), (1, 0)],
    3: [(0, 1), (0, -1)], 4: [(-1, 0), (0, 1)], 5: [(0, 1), (1, 0)],
    6: [(0, -1), (1, 0)], 7: [(-1, 0), (0, -1)]
}

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    visited = {(R, C)}
    search(R, C)

    print(f'#{tc}', len(visited))
