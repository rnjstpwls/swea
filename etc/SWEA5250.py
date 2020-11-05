import heapq


def add_fuel(next, now):
    if next-now > 0:
        return next-now
    else:
        return 0


def insert_value(tup):
    cr, cc = tup[0], tup[1]
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = cr + dr, cc + dc
        if not (0 <= nr < N) or not (0 <= nc < N) or dp[nr][nc]:
            continue
        value = add_fuel(arr[nr][nc], arr[cr][cc]) + dp[cr][cc] + 1
        heapq.heappush(heap, (value, (nr, nc)))


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    dp = [[0]*N for _ in range(N)]

    heap = []
    visited = {(0, 0)}
    current = (0, 0)
    insert_value(current)
    while dp[-1][-1] == 0:
        current_value, current_address = heapq.heappop(heap)

        if dp[current_address[0]][current_address[1]]:
            continue

        dp[current_address[0]][current_address[1]] = current_value
        visited.add(current_address)
        insert_value(current_address)




    # for row in dp:
    #     print(*row)

    print(f'#{tc}', dp[N-1][N-1])