import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    # M초 K개
    N, M, K = map(int,input().split())
    waiting = list(map(int,input().split()))
    waiting.sort(reverse=True)

    idx = 1
    oven = True
    while oven:
        for _ in range(K):
            if not waiting:
                result = 'Possible'
                oven = False
                break
            now = waiting.pop()
            if now < M*idx:
                result = 'Impossible'
                oven = False
                break
        idx += 1
    print('#'+ str(tc), result)
