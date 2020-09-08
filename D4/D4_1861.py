def search(r, c, startpoint, cnt):
    global maxv, result
    if cnt > maxv:
        maxv = cnt
        result = startpoint
    elif cnt == maxv and startpoint < result:
        result = startpoint



    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and room[nr][nc] == room[r][c] + 1:
            search(nr, nc, startpoint, cnt+1)



T = int(input())

for tc in range(1,T+1):
    N = int(input())

    room = [list(map(int,input().split())) for _ in range(N)]
    maxv = 0
    result = room[0][0]

    for i in range(N):
        for j in range(N):
            search(i,j, room[i][j], 1)
    print(f'#{tc}', result, maxv)