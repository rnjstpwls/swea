import sys
sys.stdin = open('input.txt','r')

num = 2
sosu = []

while num < 1000:
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        sosu.append(num)
    num += 1
length = len(sosu)

T = int(input())


for test_case in range(1,T+1):
    N = int(input())
    cnt = 0
    for i in range(length):
        for j in range(i,length):
            for k in range(j,length):
                if sosu[i]+sosu[j]+sosu[k] == N:
                    cnt += 1
    print(f'#{test_case} {cnt}')