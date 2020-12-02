import sys


def quarter_search(idx, total):
    global result

    if idx >= 12:
        result = min(total, result)
        return

    quarter_search(idx+1, total+swimming[idx])
    quarter_search(idx+3, total+quarter)


sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    day, month, quarter, year = map(int, input().split())
    swimming = list(map(lambda x: min(int(x)*day, month), input().split()))
    result = float('inf')
    quarter_search(0, 0)
    print(f'#{tc} {min(year, result)}')