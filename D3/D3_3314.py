import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    score = list(map(int,input().split()))
    result = []
    for i in score:
        if i >=40:
            result.append(i)
        else:
            result.append(40)
    print(f'#{test_case} {sum(result)//5}')