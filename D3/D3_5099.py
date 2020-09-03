import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    pizza = list(map(int,input().split()))

    fire = []
    index = 1
    deliver = []

    for _ in range(N):
        fire.append((pizza.pop(0),index))
        index += 1

    while len(deliver) < M:
        cheese, idx = fire.pop(0)
        cheese //= 2
        if cheese == 0:
            deliver.append(idx)
            if pizza:
                fire.append((pizza.pop(0),index))
                index += 1
        else:
            fire.append((cheese,idx))
    print(f'#{tc}', deliver[-1])