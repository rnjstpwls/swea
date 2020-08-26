import sys
sys.stdin = open('input.txt','r')

T = int(input())
length = 10 ** 6
num = [1] * (length + 1)
num[0] = 0

for i in range(3,length,2):
    for j in range(i, length+1, i):
        num[j] += i

for i in range(1,length):
    num[i+1] += num[i]


for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = num[M] - num[N-1]

    print(f'#{tc} {result}')
