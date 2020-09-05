import sys
sys.stdin = open('input.txt','r')

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())

    y = N - M
    x = M - y

    print(f'#{tc}', x, y)