import sys
sys.stdin = open('input.txt','r')

def bfs(i, j):
    queue = []
    visited = [[0]*16 for _ in range(16)]
    visited[i][j] = 1

    queue.append((i, j))
    while queue:
        i, j = queue.pop(0)
        if maze[i][j] == '3':
            return 1
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni, nj = i+di, j+dj
            if maze[ni][nj] != '1' and visited[ni][nj] == 0:
                queue.append((ni,nj))
                visited[ni][nj] = visited[i][j]+1
    return 0


def start_search():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                return bfs(i, j)


for _ in range(10):
    tc = int(input())
    maze = [input() for _ in range(16)]

    print(f'#{tc}', start_search())