def search(idx):
    visited[idx] = True

    for i in link[idx]:
        if visited[i] == False:
            search(i)

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    link = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int,input().split())
        link[a].append(b)
        link[b].append(a)

    cnt = 0
    visited = [False] * (N+1)

    for i in range(1,N+1):
        if visited[i] == False:
            search(i)
            cnt += 1
    print(f'#{tc}', cnt)
