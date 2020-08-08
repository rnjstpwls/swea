import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    N, Q = map(int,input().split())
    result = [0]*N
    # print(result)
    for i in range(1,Q+1):
        L, R = map(int,input().split())
        for j in range(L-1,R):
            result[j] = i

    print(f'#{test_case}',end=' ')
    for i in result:
        print(i,end=' ')
    print()