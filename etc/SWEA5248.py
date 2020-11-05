from collections import deque


def search(idx):
    q = deque()
    q.append(idx)
    visited[idx] = True

    while q:
        current = q.popleft()
        for i in link[current]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    link = [[] for _ in range(N+1)]
    numbers = list(map(int, input().split()))
    for i in range(M):
        link[numbers[2*i]].append(numbers[2*i+1])
        link[numbers[2*i+1]].append(numbers[2*i])
    visited = [False] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            search(i)
            cnt += 1
    print(f'#{tc}', cnt)
