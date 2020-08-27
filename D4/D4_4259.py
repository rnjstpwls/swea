import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int,input().split()))
    result = 0
    for number in numbers:
        result += (number//10) ** (number%10)
    print(f'#{tc}', result)