import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    li = list(map(int,input().split()))
    li.sort()

    if li[1] == li[0]:
        result = li[-1]
    else:
        result = li[0]

    print(f'#{test_case} {result}')