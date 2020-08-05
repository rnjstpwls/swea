import sys
sys.stdin = open('input.txt','r')

def return_max(a, b):
    if a >= b:
        return a
    else:
        return b

for test_case in range(1, 11):
    tc = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int,input().split())))

    result = 0
    for i in range(100):
        result += arr[i][i]

    total = 0
    for i in range(100):
        total += arr[i][99-i]
    result = return_max(result, total)

    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]
        result = return_max(result, total)

    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[j][i]
        result = return_max(result, total)

    print('#%d' %tc, result)
