import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    n, a, b = map(int, input().split())
    result = a + b - n
    if result < 0:
        result = 0
    print('#%d' %test_case, min(a,b), result)