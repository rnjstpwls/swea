import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    submit = list(map(int,input().split()))
    students = [i for i in range(1,N+1)]
    for i in range(K):
        students.remove(submit.pop())
    print(f'#{test_case}',end=' ')
    for i in students:
        print(i,end=' ')
    print()