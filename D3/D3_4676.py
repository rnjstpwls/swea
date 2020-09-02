import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    txt = input()
    L = len(txt)
    H = int(input())
    where = list(map(int,input().split()))
    hypen = [0]*(L+1)
    for i in where:
        hypen[i] += 1
    result = []
    for i in range(L):
        if hypen[i]:
            result.append('-'*hypen[i])
        result.append(txt[i])
    if hypen[L]:
        result.append('-'*hypen[L])
    print(f'#{tc}',''.join(result))