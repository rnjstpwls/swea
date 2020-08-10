import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    L, U, X = map(int,input().split())

    if U < X:
        result = -1
    elif L <= X <= U:
        result = 0
    else:
        result = L-X
    print(f'#{test_case} {result}')