import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    score = list(map(int,input().split()))
    score.sort()
    result = 0
    for _ in range(K):
        result += score.pop()
    print(f'#{tc}', result)