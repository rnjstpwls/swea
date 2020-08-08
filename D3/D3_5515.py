import sys
sys.stdin = open('input.txt','r')

T = int(input())
day_31 = [1,3,5,7,8,10,12]
day_30 = [4,6,9,11]
for test_case in range(1,T+1):
    m, d = map(int,input().split())
    cnt = 0

    while m != 1:
        m -= 1
        if m in day_30:
            cnt += 30
        if m in day_31:
            cnt += 31
        if m == 2:
            cnt += 29

    while d != 1:
        cnt += 1
        d -= 1
    print(f'#{test_case} {(4+cnt) % 7}')
