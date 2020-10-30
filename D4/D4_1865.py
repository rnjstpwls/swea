def search(idx, total):
    global result
    if idx == N:
        result = max(result, total)
        return
    if total <= result:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            search(idx+1, total*probability[idx][i])
            visited[i] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    probability = list(list(map(lambda x: int(x)/100, input().split())) for _ in range(N))
    visited = [False] * N
    result = 0
    search(0, 100)
    print(f'#{tc} {result:.6f}')