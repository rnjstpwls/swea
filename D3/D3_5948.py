import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1,T+1):
    num = list(map(int,input().split()))
    length = len(num)
    result = []

    for i in range(1<<length):
        cnt = 0
        total = 0
        for j in range(length):
            if i & (1<<j):
                cnt += 1
                if cnt == 4:
                    break
                total += num[j]
            else:
                continue
        if cnt == 3:
            result.append(total)
    result = list(set(result))
    result.sort(reverse=True)
    print(f'#{test_case} {result[4]}')