import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):

    text = [list(input()) for _ in range(5)]
    # print(text)

    length = len(text[0])
    for i in range(1,5):
        if len(text[i]) > length:
            length = len(text[i])
    # print(length)
    for i in range(5):
        for j in range(length-len(text[i])):
            text[i].append('*')
    # for row in text:
    #     print(*row)
    print('#%d'%test_case,end=' ')
    for i in range(length):
        for j in range(5):
            if text[j][i] == '*':
                continue
            print(text[j][i],end='')
    print()