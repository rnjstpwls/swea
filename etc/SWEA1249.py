import heapq


def search(point):
    cr, cc = point[0], point[1]
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = cr + dr, cc + dc
        if not (0 <= nr < N) or not (0 <= nc < N) or (nr, nc) in visited:
            continue
        heapq.heappush(heap, (dp[cr][cc] + arr[nr][nc], (nr, nc)))


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(list(map(int, list(input()))) for _ in range(N))
    dp = [[0] * N for _ in range(N)]

    visited = {(0, 0)}
    heap = []
    search((0, 0))
    while not dp[N - 1][N - 1]:
        value, new_point = heapq.heappop(heap)
        if dp[new_point[0]][new_point[1]]:
            continue
        dp[new_point[0]][new_point[1]] = value
        visited.add(new_point)
        search(new_point)
    print(f'#{tc}', dp[-1][-1])
