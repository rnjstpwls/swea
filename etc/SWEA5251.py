T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    link = [[] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        link[s].append((e, w))

    selected = [0]
    dp = [0] * (N+1)
    while dp[-1] == 0:
        find_min = float('inf')
        choice = (0, 0)
        for element in selected:
            for i in range(len(link[element])):
                last, weight = link[element][i]
                if last not in selected and weight < find_min:
                    find_min = weight
                    choice = (element, last)

        selected.append(choice[1])
        dp[choice[1]] = dp[choice[0]] + find_min
    print(f'#{tc}', dp[-1])