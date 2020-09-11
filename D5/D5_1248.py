import sys
sys.stdin = open('input.txt','r')

def ancestor():
    for x in parent_x:
        for y in parent_y:
            if x == y:
                return x


def pre_order(idx):
    global cnt

    if idx > V:
        return
    cnt += 1

    for i in range(2):
        if tree[idx][i]:
            pre_order(tree[idx][i])

T = int(input())

for tc in range(1,T+1):
    V, E, X, Y = map(int,input().split())
    info = list(map(int,input().split()))

    tree = [[0]*2 for _ in range(V+1)]
    parent = [0] * (V+1)
    for i in range(E):
        if tree[info[2*i]][0]:
            tree[info[2*i]][1] = info[2*i+1]
        else:
            tree[info[2*i]][0] = info[2*i+1]
        parent[info[2*i+1]] = info[2*i]

    parent_x = []
    parent_y = []

    while X:
        parent_x.append(parent[X])
        X = parent[X]
    while Y:
        parent_y.append(parent[Y])
        Y = parent[Y]

    result = ancestor()

    cnt = 0
    pre_order(result)

    print(f'#{tc}',result,cnt)