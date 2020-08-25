import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    number = int(input())
    cnt = 0
    while True:
        if number < 10:
            break

        tmp = number%10
        number //= 10
        tmp += number%10
        number //= 10
        if tmp >= 10:
            number = number*100 + tmp
        else:
            number = number*10 + tmp

        cnt += 1

    if cnt%2:
        print(f'#{tc} A')
    else:
        print(f'#{tc} B')