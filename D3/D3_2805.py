import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    farm = [input() for _ in range(N)]

    center = N//2
    result = 0
    for i in range(N):
        for j in range(N):
            if abs(i-center)+abs(j-center) <= center:
                result += int(farm[i][j])
    print(f'#{tc}', result)
