import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    people = input()

    length = len(people)
    clap = []
    for i in range(length):
        clap.append(int(people[i]))
    # print(clap)

    cnt = 0
    albamon = 0
    if clap[0] == 0:
        albamon += 1
        cnt += 1
    for i in range(0,length):
        if i > cnt:
            albamon += 1
            cnt += 1
        cnt += clap[i]
    print(f'#{test_case} {albamon}')


