def search(n, N, K, m):
    global minV
    if n == N:
        if minV > m - K and m >= K:
            minV = m - K
    elif m >= K and minV <= m - K:
        return

    else:
        search(n+1, N, K, m)
        search(n+1, N, K, m+H[n])


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    minV = 10000 * N
    search(0, N, K, 0)
    print(f'#{tc}', minV)