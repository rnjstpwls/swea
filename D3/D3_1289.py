import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    memory = input()
    cnt = 0
    for i in range(len(memory)-1):
        if memory[i+1] != memory[i]:
            cnt += 1
    if memory[0] == '1':
        cnt += 1
    print(f'#{test_case} {cnt}')