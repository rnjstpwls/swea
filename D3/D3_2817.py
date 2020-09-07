import sys
sys.stdin = open('input.txt','r')

def search(idx, total):
    global cnt
    if idx == N:
        if total == K:
            cnt += 1
        return

    if total > K:
        return

    search(idx+1, total)
    search(idx+1, total+num[idx])

T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    num = list(map(int,input().split()))
    cnt = 0
    search(0,0)
    print(f'#{tc}', cnt)