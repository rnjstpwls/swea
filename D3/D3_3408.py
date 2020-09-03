import sys
sys.stdin = open('input.txt', 'r')

def S1(num):
    return (num)*(num+1)//2


def S2(num):
    return num ** 2


def S3(num):
    return num*(num+1)

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}', S1(N), S2(N), S3(N))