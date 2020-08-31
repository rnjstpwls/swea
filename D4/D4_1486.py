import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N, B = map(int,input().split())
    assist = list(map(int,input().split()))
    result = []

    for i in range(1 << N):
        total = 0
        for j in range(N):
            if i & (1 << j):
                total += assist[j]
        if total >= B:
            result.append(total)

    print(f'#{tc}',min(result)-B)
