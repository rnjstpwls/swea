import sys
sys.stdin = open('input.txt','r')

def sharp(x,y):
    tmp = x + y - 2
    return tmp*(tmp+1)//2 + x


def inverse_sharp(num):
    for i in range(1,300):
        for j in range(1,300):
            tmp = sharp(i,j)
            if tmp == num:
                return (i,j)
            if tmp > num:
                break


T = int(input())

for tc in range(1,T+1):
    p, q = map(int,input().split())

    A = inverse_sharp(p)
    B = inverse_sharp(q)
    result = sharp(A[0]+B[0],A[1]+B[1])
    print(f'#{tc}', result)