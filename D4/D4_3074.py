import sys
sys.stdin = open('input.txt')

def search(start, end):
    if end - start <= 1:
        return

    middle = (start + end) // 2
    tmp = 0
    for g in gate:
        tmp += middle // g
    if tmp >= M:
        result.append(middle)
        end = middle
        search(start, end)
    else:
        start = middle
        search(start, end)


T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    gate = list(int(input()) for _ in range(N))
    start = 0
    end = max(gate) * M
    result = []
    search(start, end)
    print(f'#{tc}',min(result))
