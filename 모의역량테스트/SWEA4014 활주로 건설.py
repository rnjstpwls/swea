import sys
from collections import deque

def check(arr):
    stack = deque()
    flag = 0
    for i in range(N):
        if flag:
            flag -= 1
            if flag == 0:
                stack.clear()
                for k in range(1, X+1):
                    if i+k < N and arr[i+k] == arr[i] + 1:
                        return False
                stack.append(arr[i])
            continue

        if not stack:
            stack.append(arr[i])
            continue
        if stack[-1] == arr[i]:
            stack.append(arr[i])
            continue
        if stack[-1] + 1 == arr[i]:
            if len(stack) >= X:
                stack.clear()
                stack.append(arr[i])
            else:
                return False
            continue
        if stack[-1] == arr[i] + 1:
            for j in range(1, X):
                if i+j < N and arr[i+j] == arr[i]:
                    continue
                else:
                    return False
            flag = X-1
            continue
        return False
    else:
        return True







sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    result = 0
    for i in range(N):
        if check(arr[i]):
            result += 1

    for i in range(N):
        tmp = [0]*N
        for j in range(N):
            tmp[j] = arr[j][i]
        if check(tmp):
            result += 1

    print(f'#{tc}', result)