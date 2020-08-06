import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    p, q = map(float, input().split())

    # s2 올바름x 반대 올바름o
    s2 = p*(1-q)*q
    # s1 반대 올바름o
    s1 = (1-p)*q
    print(f'#{test_case}',end=' ')
    if s1 < s2:
        print('YES')
    else:
        print('NO')