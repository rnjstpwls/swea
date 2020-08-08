import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    # 1 <= X <= 10**6
    first = 1
    last = 10**6

    result = -1

    while True:
        center = (first+last)//2
        if last**3 < N or N < first ** 3:
            break
        if center ** 3 == N:
            result = center
            break
        if center ** 3 < N:
            first = center + 1
            continue
        if center ** 3 > N:
            last = center - 1
            continue
    print(f'#{test_case} {result}')