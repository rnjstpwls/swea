import sys
sys.stdin = open('input.txt', 'r')

# 이름인지 확인하는 함수
def name_check(sentence):
    result = 0
    word = list(sentence.split())
    for i in word:
        cnt = 0
        if len(i) == 1:
            if ord('A') <= ord(i[0]) <= ord('Z'):
                result += 1
        if ord('A') <= ord(i[0]) <= ord('Z'):
            for j in range(1,len(i)):
                if ord('a') <= ord(i[j]) <= ord('z'):
                    cnt += 1
                if cnt == len(i) - 1:
                    result += 1
    return result

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    gudu = ['.','?','!']
    talk = input()

    sentence = []
    
    # 구두문이 나오면 talk split하고 sentence list에 저장한다. 문장의 수인 N번만큼 반복
    for i in range(N):
        for index, j in enumerate(talk):
            if j in gudu:
                sentence += [talk[0:index]]
                # print(sentence)
                talk = talk[index+1:]
                break
                # print(talk)

    # print(sentence)
    # 공백제거
    for i in range(N):
        sentence[i] = sentence[i].strip(' ')

    print(f'#{test_case}',end=' ')
    for i in range(N):
        print(name_check(sentence[i]),end=' ')
    print()

