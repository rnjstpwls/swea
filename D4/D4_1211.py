import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0]
dy = [0, 0, 1]

def dfs(x,y):
    visited.append((x,y))
    if y == 99:
        return
    for i in range(3):
        if x+dx[i] < 0 or 99 < x+dx[i]:
            continue
        if ladder[y+dy[i]][x+dx[i]] and not ((x+dx[i], y+dy[i]) in visited):
            dfs(x+dx[i], y+dy[i])
            break


for _ in range(10):
    tc = input()
    ladder = [list(map(int,input().split())) for _ in range(100)]
    start_y = 0
    find_x = -1
    shortcut = 10000
    for i in range(100):
        if ladder[start_y][i] == 0:
            continue
        visited = []
        result = dfs(i, start_y)
        length = len(visited)
        if length < shortcut:
            find_x = i
            shortcut = length
    print('#'+tc, find_x)
