import sys
sys.stdin = open('input.txt','r')

def search(col, up, down, cnt):
    global result
    if cnt == N:
        result += 1
    for i in range(N):
        if not col[i] and not up[cnt+i] and not down[cnt-i+N-1]:
            col[i] = True
            up[cnt+i] = True
            down[cnt-i+N-1] = True
            search(col,up,down,cnt+1)
            col[i] = False
            up[cnt+i] = False
            down[cnt-i+N-1] = False

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    result = 0
    col = [False] * N
    cross_up = [False] * (2*N-1)
    cross_down = [False] * (2*N-1)
    search(col, cross_up, cross_down, 0)
    print(f'#{tc}', result)