import sys
sys.stdin = open('input.txt', 'r')

def dfs(x, y):
    global result
    visited.append((x,y))
    dx = [-1, 1, 0]
    dy = [0, 0, -1]
    if y == 0:
        result = x
        return

    for i in range(3):
        if x+dx[i] < 0 or 99 < x+dx[i]:
            continue
        if ladder[y+dy[i]][x+dx[i]] and not ((x+dx[i], y+dy[i]) in visited):
            dfs(x+dx[i],y+dy[i])
            break


for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    position_y = 99
    position_x = ladder[-1].index(2)
    visited = []
    result = 0

    dfs(position_x, position_y)
    print(f'#{tc} {result}')
