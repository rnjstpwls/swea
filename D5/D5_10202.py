import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    txt = list(input() for _ in range(3))
    # print(txt)

    result = 0

    for i in range(N):
        alphabet = [0] * 26
        for j in txt:
            alphabet[ord(j[i]) - ord('a')] += 1
        result += (3 - max(alphabet))
    print(f'#{tc}',result)