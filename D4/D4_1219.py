import sys
sys.stdin = open('input.txt','r')

def dfs(g):
    visited[g] = True
    for i in link[g]:
        if not visited[i]:
            dfs(i)

for _ in range(10):
    tc, N = map(int,input().split())
    info = list(map(int, input().split()))
    link = [[] for _ in range(100)]
    for i in range(N):
        link[info[2*i]].append(info[2*i+1])
    visited = [False] * 100

    dfs(0)
    print(f'#{tc} {int(visited[99])}')
