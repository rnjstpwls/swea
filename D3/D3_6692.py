import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    result = 0
    for case in range(N):
        p_str, x_str = input().split()
        p = float(p_str)
        x = int(x_str)
        result += p*x
    print(f'#{test_case} {result}')
