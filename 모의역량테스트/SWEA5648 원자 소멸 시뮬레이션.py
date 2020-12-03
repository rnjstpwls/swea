import sys
from collections import deque

def search(i, j):
    A_x, A_y, A_dir, A_size = atoms[i]
    B_x, B_y, B_dir, B_size = atoms[j]
    if A_x == B_x:
        if (A_y > B_y and A_dir == 1 and B_dir == 0) or (A_y < B_y and A_dir == 0 and B_dir == 1):
            collisions.append((abs(A_y-B_y), i, j, A_size, B_size))
        return
    elif A_y == B_y:
        if (A_x > B_x and A_dir == 2 and B_dir == 3) or (A_x < B_x and A_dir == 3 and B_dir == 2):
            collisions.append((abs(A_x-B_x), i, j, A_size, B_size))
        return
    elif abs(A_x-B_x) == abs(A_y-B_y):
        if (A_x > B_x) and (A_y > B_y):
            if ((A_dir == 1) and (B_dir == 3)) or ((A_dir == 2) and (B_dir == 0)):
                collisions.append((abs(A_x-B_x) + abs(A_y-B_y), i, j, A_size, B_size))
            return
        elif (A_x > B_x) and (A_y < B_y):
            if ((A_dir == 0) and (B_dir == 3)) or ((A_dir == 2) and (B_dir == 1)):
                collisions.append((abs(A_x-B_x) + abs(A_y-B_y), i, j, A_size, B_size))
            return
        elif (A_x < B_x) and (A_y > B_y):
            if ((A_dir == 3) and (B_dir == 0)) or ((A_dir == 1) and (B_dir == 2)):
                collisions.append((abs(A_x-B_x) + abs(A_y-B_y), i, j, A_size, B_size))
            return
        elif (A_x < B_x) and (A_y < B_y):
            if ((A_dir == 3) and (B_dir == 1)) or ((A_dir == 0) and (B_dir == 2)):
                collisions.append((abs(A_x-B_x) + abs(A_y-B_y), i, j, A_size, B_size))
            return
    else:
        return



sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    atoms = [tuple(map(int, input().split())) for _ in range(N)]

    collisions = []

    for i in range(N-1):
        for j in range(i+1, N):
            search(i, j)

    collisions = deque(sorted(collisions))

    visited = [0] * N
    result = 0
    while collisions:
        time, A, B, A_size, B_size = collisions.popleft()
        if visited[A] == 0 and visited[B] == 0:
            result += A_size
            result += B_size
            visited[A] = time
            visited[B] = time
        elif visited[A] == time and visited[B] == 0:
            result += B_size
            visited[B] = time
        elif visited[B] == time and visited[A] == 0:
            result += A_size
            visited[A] = time
        else:
            continue
    print(f'#{tc}', result)