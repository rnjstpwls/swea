import sys
sys.stdin = open('input.txt', 'r')

def rise_check(value):
    tmp = []
    tmp_num = value

    if value < 10:
        return value

    else:
        while value//10 != 0:
            tmp.append(value%10)
            value //= 10
        tmp.append(value)
        for i in range(len(tmp) - 1):
            if tmp[i] < tmp[i+1]:
                return -1
        return tmp_num



T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    num = list(map(int,input().split()))

    find_max = -1

    for i in range(N-1):
        for j in range(i+1,N):
            if rise_check(num[i]*num[j]) > find_max:
                find_max = rise_check(num[i]*num[j])

    print(f'#{test_case} {find_max}')
