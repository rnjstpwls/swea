import sys
sys.stdin = open('input2.txt','r')

def bfs(r,c):
    queue = []
    visited = [[0]*N for _ in range(N)]
    queue.append((r,c))
    while queue:
        cr, cc = queue.pop(0)
        if maze[cr][cc] == '3':
            return visited[cr][cc] - 1
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            if (0 <= cr+dr < N) and (0 <= cc+dc < N) and maze[cr+dr][cc+dc] != '1' and visited[cr+dr][cc+dc] == 0:
                queue.append((cr+dr,cc+dc))
                visited[cr+dr][cc+dc] = visited[cr][cc] + 1

    return 0


def start_search():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return bfs(i,j)


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    print(f'#{tc}', start_search())
