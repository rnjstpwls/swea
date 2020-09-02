import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    card = list(input().split())
    A = card[0:(N+1)//2]
    B = card[(N+1)//2:N]
    # print(A)
    # print(B)
    result = []
    while len(result) != N:
        if A:
            result.append(A.pop(0))
        if B:
            result.append(B.pop(0))
    print(f'#{tc}', *result)