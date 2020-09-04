import sys
sys.stdin = open('input.txt','r')

def search(r, c, cnt, num):
    if cnt == 7:
        result.append(num)
        return

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            search(nr, nc, cnt+1, num+arr[nr][nc])



for tc in range(1, int(input())+1):
    arr = [list(input().split()) for _ in range(4)]
    result = []

    for i in range(4):
        for j in range(4):
            search(i,j,1,arr[i][j])

    print(f'#{tc}',len(set(result)))