import sys

sys.stdin = open('input.txt')


direction = {
    1: (-1, 0), 2: (1, 0),
    3: (0, -1), 4: (0, 1)
}


T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    bug_dict = dict()
    for _ in range(K):
        r, c, cnt, d = map(int, input().split())
        bug_dict[(r, c)] = [(cnt, direction[d])]
    for _ in range(M):
        new_dict = dict()
        for key, value in bug_dict.items():
            cr, cc = key
            bug_cnt, dr, dc = value[0][0], value[0][1][0], value[0][1][1]
            nr, nc = cr+dr, cc+dc

            if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                bug_cnt //= 2
                dr *= -1
                dc *= -1
            if not bug_cnt:
                continue

            if (nr, nc) in new_dict:
                new_dict[(nr, nc)].append((bug_cnt, (dr, dc)))
            else:
                new_dict[(nr, nc)] = [(bug_cnt, (dr, dc))]
        for i in new_dict:
            if len(new_dict[i]) > 1:
                total = 0
                next_dir = (0, 0)
                find_max = 0
                for bugs, current_dir in new_dict[i]:
                    total += bugs
                    if bugs > find_max:
                        find_max = bugs
                        next_dir = current_dir
                new_dict[i] = [(total, next_dir)]
        bug_dict = new_dict

    result = 0
    for i in bug_dict:
        result += bug_dict[i][0][0]
    print(f'#{tc}', result)