T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    vote = [0]*(N)
    for b in B:
        for i in range(len(A)):
            if A[i] <= b:
                vote[i] += 1
                break
            else:
                continue
    print(f'#{tc}', vote.index(max(vote))+1)