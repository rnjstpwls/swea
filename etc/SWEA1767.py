def search(idx, total, cnt):
    global result, total_core
    if idx == core_cnt:
        if cnt > total_core:
            result = total
            total_core = cnt
        elif cnt == total_core:
            result = min(result, total)
        return

    cr, cc = core[idx]
    # already connected
    if cr == 0 or cc == 0 or cr == N - 1 or cc == N - 1:
        search(idx + 1, total, cnt + 1)
    else:
        search(idx + 1, total, cnt)

        for r in range(cr):
            nr = cr - r - 1
            if arr[nr][cc]:
                break
        else:
            for r in range(cr):
                nr = cr - r - 1
                arr[nr][cc] = 1
            search(idx + 1, total + cr, cnt + 1)
            for r in range(cr):
                nr = cr - r - 1
                arr[nr][cc] = 0

        for r in range(N - cr - 1):
            nr = cr + r + 1
            if arr[nr][cc]:
                break
        else:
            for r in range(N - cr - 1):
                nr = cr + r + 1
                arr[nr][cc] = 1
            search(idx + 1, total + N - cr - 1, cnt + 1)
            for r in range(N - cr - 1):
                nr = cr + r + 1
                arr[nr][cc] = 0

        for c in range(cc):
            nc = cc - c - 1
            if arr[cr][nc]:
                break
        else:
            for c in range(cc):
                nc = cc - c - 1
                arr[cr][nc] = 1
            search(idx + 1, total + cc, cnt + 1)
            for c in range(cc):
                nc = cc - c - 1
                arr[cr][nc] = 0

        for c in range(N - cc - 1):
            nc = cc + c + 1
            if arr[cr][nc]:
                break
        else:
            for c in range(N - cc - 1):
                nc = cc + c + 1
                arr[cr][nc] = 1
            search(idx + 1, total + N - cc - 1, cnt + 1)
            for c in range(N - cc - 1):
                nc = cc + c + 1
                arr[cr][nc] = 0


def search_core():
    tmp = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                tmp.append((r, c))
    return tmp


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    core = search_core()
    core_cnt = len(core)

    result = 9876543210
    total_core = -1
    search(0, 0, 0)
    print('#{} {}'.format(tc, result))
