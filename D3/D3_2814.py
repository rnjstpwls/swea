import sys
sys.stdin = open('input.txt','r')

def search(point, visited):
    global max_length
    if len(visited) > max_length:
        max_length = len(visited)

    for i in link[point]:
        if i not in visited:
            search(i, visited+[i])
    pass

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    link = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int,input().split())
        link[x].append(y)
        link[y].append(x)
    # print(link)
    max_length = 1

    for i in range(1,N):
        search(i,[i])
    print(f'#{tc}', max_length)