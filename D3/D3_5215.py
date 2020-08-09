import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    N, L = map(int,input().split())
    info = []
    for i in range(N):
        info.append(list(map(int,input().split())))
    # print(info)

    result = []

    for i in range(1<<N):
        score = 0
        calorie = 0
        for j in range(N):
            if (1<<j) & i:
                score += info[j][0]
                calorie += info[j][1]
        if calorie <= L:
            result.append(score)

    print(f'#{test_case} {max(result)}')
