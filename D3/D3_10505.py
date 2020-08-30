import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    incomes = list(map(int,input().split()))
    avg = sum(incomes)/N

    cnt = 0
    for income in incomes:
        if income <= avg:
            cnt += 1
    print(f'#{tc} {cnt}')