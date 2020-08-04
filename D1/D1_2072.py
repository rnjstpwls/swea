import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    li = list(map(int, input().split()))
    total = 0
    for i in li:
        if i%2:
            total += i

    print('#%d' %test_case, total)


