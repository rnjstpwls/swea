import sys
sys.stdin = open('input.txt','r')

def bfs(k):
    queue = []
    visited[k] = 1
    queue.append(k)
    while queue:
        c = queue.pop(0)
        for i in link[c]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[c] + 1


for tc in range(1,11):
    length, start = map(int,input().split())
    info = list(map(int,input().split()))
    link = [[] for _ in range(101)]
    for i in range(0,length,2):
        link[info[i]].append(info[i+1])


    visited = [0] * 101
    bfs(start)

    visited.reverse()
    print(f'#{tc}',100 - visited.index(max(visited)))