T = int(input())

for tc in range(1,T+1):
    N = int(input())

    cost = sorted(list(map(int, input().split())), reverse=True)
    total = 0
    for i in range(N//3):
        total += cost[2+3*i]
    print(f'#{tc}', sum(cost) - total)
