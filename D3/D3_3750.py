import sys
sys.stdin = open('input.txt','r')

def digit_sum(num):
    if num < 10:
        return num

    total = 0
    while num > 0:
        total += num%10
        num //= 10
    return digit_sum(total)


T = int(input())
result = []
for tc in range(1,T+1):
    num = int(input())
    result.append(digit_sum(num))
for i in range(T):
    print(f'#{i+1}', result[i])