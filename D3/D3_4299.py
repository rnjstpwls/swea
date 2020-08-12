import sys
sys.stdin = open('input.txt','r')

T = int(input())

bebelo = 11

for test_case in range(1,T+1):
    D, H, M = map(int,input().split())
    result = (M-bebelo) + 60*(H-bebelo) + 1440*(D-bebelo)
    if result < 0:
        result = -1
    print(f'#{test_case} {result}')