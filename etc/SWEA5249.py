from collections import deque


def master(idx):
    if check[idx] == idx:
        return idx
    else:
        return master(check[idx])


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    V += 1

    info = deque(sorted(list(tuple(map(int, input().split())) for _ in range(E)), key=lambda x: x[2]))
    # print(info)
    check = list(range(V))

    result = 0
    cnt = 0
    while info:
        n1, n2, w = info.popleft()
        if master(n1) != master(n2):
            result += w
            cnt += 1

            check[master(n2)] = master(n1)

            if cnt == V - 1:
                break

    print(f'#{tc}', result)
