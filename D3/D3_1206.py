import sys

sys.stdin = open("input.txt", "r")


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    a = int(input())
    b = list(map(int, input().split()))
    cnt = 0
    for i in range(2,a-2):
        tmp_list = list()
        tmp_list += [b[i] - b[i-2]]
        tmp_list += [b[i] - b[i-1]]
        tmp_list += [b[i] - b[i+1]]
        tmp_list += [b[i] - b[i+2]]
        tmp = min(tmp_list)
        if tmp > 0:
            cnt += tmp
    print('#',end='')
    print(test_case, end=' ')
    print(cnt)


