import sys
sys.stdin = open('input.txt','r')

prime = []
for i in range(2, 10**6):
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        prime.append(i)


T = int(input())

for tc in range(1,T+1):
    D, A, B = input().split()
    A, B = int(A), int(B)
    cnt = 0
    for i in prime:
        if i < A:
            continue
        if B < i:
            break
        if D in str(i):
            cnt += 1
    print(f'#{tc}', cnt)