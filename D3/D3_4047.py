import sys
sys.stdin = open('input.txt','r')

T = int(input())
#  13
for test_case in range(1,T+1):
    S = D = H = C = 13
    txt = input()
    length = len(txt)//3

    info = []
    for i in range(length):
        info.append(txt[3*i:3*(i+1)])
    # print(info)

    for i in range(length):
        if info[i][0] == 'S':
            S -= 1
        elif info[i][0] == 'D':
            D -= 1
        elif info[i][0] == 'H':
            H -= 1
        else:
            C -= 1

    if len(list(set(info))) != len(info):
        result = 'ERROR'
    else:
        result = f'{S} {D} {H} {C}'

    print(f'#{test_case} {result}')

