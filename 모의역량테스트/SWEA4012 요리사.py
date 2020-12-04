import sys


def search(idx, select):
    global result

    if idx == N and len(select) == N//2:
        opposite_food = list(numbers_set - select)
        select = list(select)
        opposite_food_score = 0
        for i in range(N//2 - 1):
            for j in range(i+1, N//2):
                opposite_food_score += synergy[opposite_food[i]][opposite_food[j]]
                opposite_food_score += synergy[opposite_food[j]][opposite_food[i]]

        food_score = 0
        for i in range(N//2 - 1):
            for j in range(i+1, N//2):
                food_score += synergy[select[i]][select[j]]
                food_score += synergy[select[j]][select[i]]
        calculate = abs(food_score-opposite_food_score)
        result = min(result, calculate)
        return

    if idx >= N or len(select) > N//2:
        return

    search(idx+1, select | {numbers[idx]})
    search(idx+1, select)


sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    synergy = list(list(map(int, input().split())) for _ in range(N))
    numbers = list(range(N))
    numbers_set = set(range(N))

    result = float('inf')
    search(1, {0})
    print(f'#{tc}', result)